import mysql.connector
import json
from flask import Flask, Blueprint, Response
from flask import jsonify, make_response, request
from flask_cors import CORS
from mysql.connector import Error
from RandomDealData import *
from deals_dao import DealsDAO
from probes_dao import ProbesDAO
from instruments_dao import InstrumentsDAO
from balance_dao import BalanceDAO

app = Flask(__name__)
# app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

deals_dao = DealsDAO()
probes_dao = ProbesDAO()
instruments_dao = InstrumentsDAO()


@app.route('/connection_check', methods=["GET"])
def connection_check():
    """ Connect to MySQL database """
    try:
        if probes_dao.check_connection():
            data = {'message': 'Connected', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/login_check', methods=["POST"])
def login_check():
    try:
        if probes_dao.check_login(request.json.get('login'),request.json.get('password')):
            data = {'message': 'Credentials valid', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)
        data = {'message': 'Credentials invalid', 'code': 'Unauthorized'}
        return make_response(jsonify(data), 401)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


# TODO: pagination ?
@app.route('/deals/history', methods=['GET'])
def get_persisted_deals():
    try:
        result = deals_dao.get_all_deals()
        return make_response(jsonify(result), 200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


# TODO: pagination ?
@app.route('/deals/history/<instrument>', methods=['GET'])
def query_persisted_deals(instrument):
    try:
        result = deals_dao.filter_deals_by_instrument(instrument)
        return make_response(jsonify(result), 200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/deals/stream', methods=['GET'])
def get_real_time_deals():
    return Response(deal_stream, status=200, mimetype="text/event-stream")

@app.route('/instruments', methods=['GET'])
def get_instruments_names():
    try:
        result = instruments_dao.get_all_instrument_names()
        return make_response(jsonify(result), 200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/instruments/average_price', methods=['GET'])
def get_instruments_average_price():
    try:
        result = instruments_dao.get_all_instrument_average_prices()
        return make_response(jsonify(result), 200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/instruments/ending_position', methods=['GET'])
def get_instruments_ending_position():
    try:
        result = instruments_dao.get_all_instrument_ending_positions()
        return make_response(jsonify(result), 200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/balance/realized', methods=['GET'])
def get_realized_profit_loss():
    try:
        balance_dao.get_realized_balance()
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/balance/effective', methods=['GET'])
def get_effective_profit_loss():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            # TODO: while persisiting - keep track of effective profit/loss

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()

@app.route('/streamTest')
def stream():
    return Response(deal_stream, status=200, mimetype="text/event-stream")


def persist_data(nextId, next):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"INSERT into deal "
                           f"VALUES  ({nextId}, "
                           f"'{next['time']}', "
                            f"(SELECT counterparty_id FROM counterparty WHERE counterparty_name = '{next['cpty']}'), "
                            f"(SELECT instrument_id FROM instrument WHERE instrument_name = '{next['instrumentName']}'), " 
                            f"'{next['type']}', "
                            f"{next['price']}, "
                            f"{next['quantity']})")
            conn.commit()
    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        #return (jsonify(data), 500)
        print(e)
    finally:
        cursor.close()
        conn.close()

def deal_generator(rdd, instrList):
    while True:
        nextId, next = rdd.createRandomData(instrList)
        persist_data(nextId, next)
        #print("Persisting {}".format(next))
        # nonlocal instrList

        yield 'data:{}\n\n'.format(json.dumps(next))




def bootapp():
    app.run(port=8090, threaded=True, host=('localhost'))



if __name__ == '__main__':
    rdd = RandomDealData()
    instrList = rdd.createInstrumentList()
    global deal_stream
    deal_stream = deal_generator(rdd, instrList)
    bootapp()

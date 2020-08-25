import mysql.connector
import json
from flask import Flask, Blueprint, Response
from flask import jsonify, make_response, request
from flask_cors import CORS
from mysql.connector import Error
from RandomDealData import *

app = Flask(__name__)
# app.register_blueprint(sse, url_prefix='/stream')
CORS(app)


@app.route('/connection_check', methods=["GET"])
def connection_check():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')
        if conn.is_connected():
            data = {'message': 'Connected', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        conn.close()


@app.route('/login_check', methods=["POST"])
def login_check():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM users where user_id='{request.json.get('login')}' and user_pwd='{request.json.get('password')}'")
            cursor.fetchall()
            if cursor.rowcount == 1:
                data = {'message': 'Credentials valid', 'code': 'SUCCESS'}
                return make_response(jsonify(data), 200)
            data = {'message': 'Credentials invalid', 'code': 'Unauthorized'}
            return make_response(jsonify(data), 401)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


# TODO: pagination ?
@app.route('/deals/history', methods=['GET'])
def get_persisted_deals():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "deal_time,"
                "instrument_name,"
                "counterparty_name,"
                "deal_type,"
                "deal_quantity,"
                "deal_price "
                "FROM "
                "deal join "
                "instrument  on deal.deal_instrument_id=instrument.instrument_id join "
                "counterparty on deal.deal_counterparty_id=counterparty.counterparty_id")
            result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
            return make_response(jsonify(result), 200)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


# TODO: pagination ?
@app.route('/deals/history/<instrument>', methods=['GET'])
def query_persisted_deals(instrument):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "deal_time,"
                "instrument_name,"
                "counterparty_name,"
                "deal_type,"
                "deal_quantity,"
                "deal_price "
                "FROM "
                "deal join "
                "instrument  on deal.deal_instrument_id=instrument.instrument_id join "
                "counterparty on deal.deal_counterparty_id=counterparty.counterparty_id "
                "WHERE "
                f"instrument_name='{instrument}'")
            result = [dict(zip(cursor.column_names, row)) for row in cursor.fetchall()]
            return make_response(jsonify(result), 200)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


@app.route('/deals/stream', methods=['GET'])
def get_real_time_deals():
    return Response(deal_stream, status=200, mimetype="text/event-stream")

@app.route('/instruments', methods=['GET'])
def get_instruments_names():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT instrument_name FROM instrument")
            result = [row[0] for row in cursor.fetchall()]
            return make_response(jsonify(result), 200)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


@app.route('/instruments/average_price', methods=['GET'])
def get_instruments_average_price():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "instrument_name, "
                "deal_type, "
                "avg(deal_price) "
                "FROM "
                "deal join "
                "instrument on deal.deal_instrument_id=instrument.instrument_id "
                "GROUP BY "
                "instrument_name,"
                "deal_type "
                "HAVING "
                "instrument_name IN (SELECT instrument_name FROM instrument)")
            instrument_prices = {}
            for row in cursor.fetchall():
                if row[0] not in instrument_prices:
                    instrument_prices[row[0]] = {"B": 0, "S": 0}
                instrument_prices[row[0]][row[1]] = row[2]
            result = [ {"name": name , "prices": { "buy": prices["B"], "sell": prices["S"]}} for name, prices in instrument_prices.items()]
            return make_response(jsonify(result), 200)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


@app.route('/instruments/ending_position', methods=['GET'])
def get_instruments_ending_position():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT "
                "instrument_name, "
                "deal_type, "
                "sum(deal_quantity) "
                "FROM "
                "deal join "
                "instrument on deal.deal_instrument_id=instrument.instrument_id "
                "GROUP BY "
                "instrument_name,"
                "deal_type "
                "HAVING "
                "instrument_name IN (SELECT instrument_name FROM instrument)")
            instrument_positions = {}
            for row in cursor.fetchall():
                if row[0] not in instrument_positions:
                    instrument_positions[row[0]] = {"B": 0, "S": 0}
                instrument_positions[row[0]][row[1]] = row[2]
            result = [ {"name": name , "prices": { "buy": positions["B"], "sell": positions["S"]}} for name, positions in instrument_positions.items() ]
            return make_response(jsonify(result), 200)

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


@app.route('/balance/realized', methods=['GET'])
def get_realized_profit_loss():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_grad_cs_1917',
                                       user='root',
                                       password='ppp')

        if conn.is_connected():
            cursor = conn.cursor()
            # TODO: while persisiting - keep track of realized profit/loss

    except Error as e:
        data = {'message': 'Not connected', 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

    finally:
        cursor.close()
        conn.close()


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

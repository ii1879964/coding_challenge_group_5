import os

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

db_host = os.getenv('DB_HOST','localhost')

deals_dao = DealsDAO(host=db_host)
probes_dao = ProbesDAO(host=db_host)
instruments_dao = InstrumentsDAO(host=db_host)

rdd = RandomDealData()


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

    def deal_generator():
        for nextId, next in rdd.deal_generator():
            BalanceDAO.recount_profit_loss(next)
            deals_dao.persist_data(nextId, next)
            yield 'data:{}\n\n'.format(json.dumps(next))

    return Response(deal_generator(), status=200, mimetype="text/event-stream")

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
        return make_response(jsonify(BalanceDAO.get_realized_balance()),200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/balance/effective', methods=['GET'])
def get_effective_profit_loss():
    try:
        return make_response(jsonify(BalanceDAO.get_effective_balance()),200)
    except Error as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))


if __name__ == '__main__':
    bootapp()

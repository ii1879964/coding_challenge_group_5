import os

import requests
from flask import Flask, Response
from flask import jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
# app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

dao_host = os.getenv('DAO_HOST', 'localhost')
dao_port = os.getenv('DAO_PORT', '8090')
dao_url = f"http://{dao_host}:{dao_port}"


@app.route('/connection_check', methods=["GET"])
def connection_check():
    """ Connect to MySQL database """
    try:
        r = requests.get(f"{dao_url}/connection_check")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/login_check', methods=["POST"])
def login_check():
    try:
        print(request.json)
        r = requests.post(f"{dao_url}/login_check", json=request.json, headers=request.headers)
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


# TODO: pagination ?
@app.route('/deals/history', methods=['GET'])
def get_persisted_deals():
    try:
        r = requests.get(f"{dao_url}/deals/history")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


# TODO: pagination ?
@app.route('/deals/history/<instrument>', methods=['GET'])
def query_persisted_deals(instrument):
    try:
        r = requests.get(f"{dao_url}/deals/history/{instrument}")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/deals/stream', methods=['GET'])
def get_real_time_deals():
    r = requests.get(f"{dao_url}/deals/stream", stream=True)

    def eventStream():
        for line in r.iter_lines(chunk_size=1):
            if line:
                print(line.decode())
                # the next lines emit the received data as a SSE
                yield line.decode()

    return Response(eventStream(), mimetype="text/event-stream")


@app.route('/instruments', methods=['GET'])
def get_instruments_names():
    try:
        r = requests.get(f"{dao_url}/instruments")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/instruments/average_price', methods=['GET'])
def get_instruments_average_price():
    try:
        r = requests.get(f"{dao_url}/instruments/average_price")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/instruments/ending_position', methods=['GET'])
def get_instruments_ending_position():
    try:
        r = requests.get(f"{dao_url}/instruments/ending_position")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/balance/realized', methods=['GET'])
def get_realized_profit_loss():
    try:
        r = requests.get(f"{dao_url}/balance/realized")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


@app.route('/balance/effective', methods=['GET'])
def get_effective_profit_loss():
    try:
        r = requests.get(f"{dao_url}/balance/effective")
        return r.content, r.status_code
    except Exception as e:
        data = {'message': e, 'code': 'Internal Server Error'}
        return make_response(jsonify(data), 500)


def bootapp():
    app.run(port=8100, threaded=True, host=('0.0.0.0'))


if __name__ == '__main__':
    bootapp()

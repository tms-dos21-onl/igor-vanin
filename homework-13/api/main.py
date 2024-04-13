from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
import random
import requests
import socket
import sys
import threading
import time

host = '0.0.0.0'
port = sys.argv[1] if len(sys.argv) > 1 else 5000

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': f"API on {host}:{port} ({socket.gethostname()})",
    'uiversion': 3,
    'openapi': '3.0.3',
}
swagger = Swagger(app)
threadLimiter = threading.BoundedSemaphore(10)


@app.route('/bigResponse')
def bigResponse():
    """Returns a big message
    ---
    responses:
      200:
        description: A response message
        schema:
          type: string
        examples:
          "Bi...ig"
    """

    return jsonify(f"B{'i' * 4 * 1000 * 1000}g")


@app.route('/delayedResponse')
def delayedResponse():
    """Returns a message after some delay
    ---
    responses:
      200:
        description: A response message
        schema:
          type: string
        examples:
          "Delayed response"
    """

    time.sleep(60 + random.randint(0, 10))

    return jsonify('Delayed response')


@app.route('/ping')
def ping():
    """Returns pong
    ---
    responses:
      200:
        description: A response message
        schema:
          type: string
        examples:
          "Pong"
    """

    with threadLimiter:
        time.sleep(1)

        return jsonify("Pong")


@app.route('/readBigResponseSlowly', methods = ['POST'])
def readBigResponseSlowly():
    """Reads the message returned by /bigResponse slowly
    ---
    responses:
      200:
        description: A response message
        schema:
          type: string
        examples:
          "Response is read"
    """

    s = requests.Session()

    with s.get(request.headers['Origin'] + '/bigResponse', headers=None, stream=True) as response:
        time.sleep(60 + random.randint(0, 10))

    return jsonify('Response is read')


@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    """Uploads a file
    ---
    requestBody:
      content:
        application/octet-stream:
          schema:
            type: string
            format: binary
    responses:
      200:
        description: A response message
        schema:
          type: string
        examples:
          "File is uploaded"
    """

    body = request.stream.read()

    return jsonify('File is uploaded')


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)

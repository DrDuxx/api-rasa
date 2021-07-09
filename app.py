from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, send
import random
import requests
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         colors = ['red', 'blue', 'yellow']
#         rand = random.randrange(0, 3)
#         return jsonify({"color": colors[rand]})
#     else:
#         body = request.get_json()
#         res = requests.post(os.environ.get("API_URL") + '/webhooks/rest/webhook', json=body)
#         final = res.json()
#         return jsonify(final[0])


@socketio.on('message')
def handleMessage(msg):
    try:
        msg
    except NameError:
        msg="hey"

    data = {"sender":"User","message":msg}
    res = requests.post(os.environ.get("API_URL") + '/webhooks/rest/webhook', json=data)
    final = res.json()
    if(len(final)>1):
        print("SEND COLOR TO MICKEL")
    send(final[0]["text"])


if __name__ == '__main__':
    socketio.run(app, port=5000)

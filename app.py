from flask import Flask, jsonify, request
import random
import requests
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        colors = ['red', 'blue', 'yellow']
        rand = random.randrange(0, 3)
        return jsonify({"color": colors[rand]})
    else:
        body = request.get_json()
        res = requests.post(os.environ.get("API_URL") + '/webhooks/rest/webhook', json=body)
        final = res.json()
        return jsonify(final[0])


if __name__ == '__main__':
    app.run(debug=True)

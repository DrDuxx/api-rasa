from flask import Flask, jsonify, request
import random
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method=='GET'):
        colors = ['red', 'blue', 'green']
        rand = random.randrange(0, 3)
        return jsonify({"color":colors[rand]})
    else:
        body = request.get_json()
        return jsonify(body)


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method=='GET'):
        return jsonify({"response":"GET RESPONSE"})
    else:
        body = request.get_json()
        # Do a request to rasa and then return the returned value
        # validate reply type and return json with important information containing the reply and some bool values
        return jsonify({"response":body})


if __name__ == '__main__':
    app.run(debug=True)


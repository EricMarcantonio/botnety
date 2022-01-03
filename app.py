from flask import Flask, request
from structs import commands
import json

command = commands.Commands()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Sanity Check</h1>'


@app.route('/api/v1/commands', methods=['POST', 'GET'])
def commands():
    data = dict()

    def validate_post() -> (str, int):
        if 'command' not in request.json:
            return "Commands list is not present.", 400
        if len(request.json) != 1:
            return "Request is not the right length.", 400
        if not isinstance(request.json['command'], list):
            return "Commands is not a list.", 400
        if len(request.json['command']) == 0:
            return "Commands array does not contain command.", 400
        if not all(isinstance(x, str) for x in request.json['command']):
            return "Commands array should only contain strings.", 400
        return "OK", 200

    if request.method == 'POST':
        msg, code = validate_post()
        if code == 200:
            command.set_commands(request.json)
        return msg, code
    else:
        data['command'] = command.get_commands_unique()

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/api/v1/commands_encrypted', methods=['GET'])
def commands_encrypted():
    data = dict()
    data['command'], data['tag'], data['key'], data['nonce'] = command.get_commands_encrypted_unique()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/api/v1/commands_decrypt', methods=['GET'])
def commands_decrypt():
    data = command.get_commands_decrypt(request.json['command'], request.json['tag'], request.json['key'], request.json['nonce'])
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

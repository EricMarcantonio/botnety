from flask import Flask, request
from structs import commands
import json
app = Flask(__name__)

commands = commands.Commands()


@app.route('/', methods=['GET'])
def home():
    return '<h1>Sanity Check</h1>'


@app.route('/api/v1/commands', methods=['POST', 'GET'])
def request_commands():
    # content = request.json
    data = dict()
    if request.method == 'POST':
        if 'commands' not in request.json:
            return "Commands list is not present.", 400
        if len(request.json) != 1:
            return "Request is not the right length.", 400
        if not isinstance(request.json['commands'], list):
            return "Commands is not a list.", 400
        if len(request.json['commands']) == 0:
            return "Commands array does not contain commands.", 400
        if not all(isinstance(x, str) for x in request.json['commands']):
            return "Commands array should only contain strings.", 400
        data['commands'] = commands.set_commands(request.json)
    else:
        data['commands'] = commands.get_commands_unique()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

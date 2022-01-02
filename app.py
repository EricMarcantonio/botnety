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
    if request.method == 'GET':
        data['commands'] = commands.get_commands_unique()
    else:
        data['commands'] = commands.set_commands(request.json)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('test.json') as f:
    data = json.load(f)


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

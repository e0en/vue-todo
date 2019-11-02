#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import ujson as json


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Hello, world!'


@app.route('/todo', methods=['POST', 'GET'])
def todo():
    return json.dumps([])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import sqlite3

from flask import Flask, request
from flask_cors import CORS
import ujson as json

from secret import DB_FILENAME


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Hello, world!'


@app.route('/todo', methods=['POST', 'GET'])
def todo():
    if request.method == 'POST':
        new_item_id = add(request.get_json())
        return new_item_id
    elif request.method == 'GET':
        return json.dumps(get_all())
    else:
        raise ValueError('Unexpected request method')
    todo_uuid = str(uuid.uuid1())
    return json.dumps([todo_uuid])


@app.route('/todo/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def todo_item(item_id: str):
    if request.method == 'GET':
        result = json.dumps(get_one(item_id))
    elif request.method == 'PUT':
        update(request.get_json())
    elif request.method == 'DELETE':
        delete(item_id)
        pass
    else:
        raise ValueError('Unexpected request method')
    item_id = str(uuid.uuid1())
    return json.dumps([item_id])


def add(form):
    item_id = str(uuid.uuid1())
    content = form['content']
    query = 'INSERT INTO todos (uuid, content) VALUES (?,?)'
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute(query, (item_id, content))
    conn.commit()
    conn.close()
    return item_id


def update(form):
    item_id = form['itemId']
    content = form['content']
    is_done = form['isComplete']
    query = 'UPDATE todos SET content=?, is_done=? WHERE uuid=?'
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute(query, (content, is_done, item_id))
    conn.commit()
    conn.close()
    return item_id


def get_all():
    query = 'SELECT uuid, content, is_done, time_create, time_edit FROM todos'
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute(query)
    result = list()
    for row in c.fetchall():
        result += [row_to_obj(row)]
    conn.close()
    return result


def get_one(item_id: str):
    query = 'SELECT uuid, content, is_done, time_create, time_edit FROM todos WHERE uuid=?'
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute(query, (item_id, ))
    result = c.fetchone()
    conn.close()
    return row_to_obj(result)


def delete(item_id: str):
    query = 'DELETE FROM todos WHERE uuid=?'
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute(query, (item_id, ))
    conn.commit()
    conn.close()


def row_to_obj(row):
    return {
        'itemId': row[0],
        'content': row[1],
        'isComplete': row[2] > 0,
        'timeCreate': row[3],
        'timeEdit': row[4],
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

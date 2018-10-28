"""Provide REST API.

Root URL: http://[hostname/]/cash/v1/

Methods:
GET http://[hostname/]/cash/v1
    Return 200 (for health checks)
GET http://[hostname/]/cash/v1/expenses
    Get expenses
GET http://[hostname/]/cash/v1/categories
    Get expense categories
GET http://[hostname/]/cash/v1/users
    GET users
POST http://[hostname/]/cash/v1/expenses
    Add a new expense
    Payload example:
    {
        "date": "2018-10-28",
        "user_id": 1,
        "category_id": 9,
        "amount": 45,
        "comment": "Hose"
    }
"""

from flask import Flask, abort, jsonify, request, flash, Response
import expenses
import logging
import traceback
import sys

ROOT_URL = "/cash/v1"

app = Flask(__name__, static_url_path='/static')
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@app.route(ROOT_URL, methods=['GET'])
def return_ok():
    return("OK")

@app.route(ROOT_URL + '/expenses', methods=['GET'])
def get_expenses():
    try:
        res = expenses.get_expenses()
    except:
        return logger.error("Cannot create a DB connection.\n{}".format(
            traceback.format_exc()))
    else:
        return Response(res, status=200, mimetype='application/json')

@app.route(ROOT_URL + '/expenses', methods=['POST'])
def post_expense():
    if (request.is_json):
        try:
            content = request.get_json()
        except:
            logger.error("Cannot parse JSON request: {}".format(
                traceback.format_exc()))
            return Response('{"message": "Cannot parse JSON request"}', status=400, mimetype='application/json')
    else:
        logger.error("Received request is not JSON")
        return Response('{"message": "Received request body is not JSON"}', status=400, mimetype='application/json')

    try:
        add_expense(content)
    except:
        logger.error("Cannot add expense to DB: {}".format(
                traceback.format_exc()))
        return Response('{"message": "Cannot add expense to DB"}', status=500, mimetype='application/json')
    else:
        return Response('{"message": "OK"}', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)

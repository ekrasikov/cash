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
from flask_cors import CORS
import expenses
import logging
import traceback
import sys
import os

ROOT_URL = "/cash/v1"

app = Flask(__name__, static_url_path='/static')
CORS(app)

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

host = os.environ.get('CASH_DB_HOST')
dbname = os.environ.get('CASH_DB_NAME')
user = os.environ.get('CASH_DB_USER')
password = os.environ.get('CASH_DB_PASSWORD')

db_params = {
    "host": host,
    "dbname": dbname,
    "user": user,
    "password": password
}


@app.route(ROOT_URL, methods=['GET'])
def return_ok():
    return("OK")


@app.route(ROOT_URL + '/expenses', methods=['GET'])
def get_expenses():
    res = expenses.get_data("expenses", db_params)
    if (not res):
        logger.error("Cannot load expenses from DB.\n{}".format(
            traceback.format_exc()))
        return Response('{"message": "Cannot load expenses from DB"}', status=500, mimetype='application/json')
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
        logger.error("Received request body is not JSON")
        return Response('{"message": "Received request body is not JSON"}', status=400, mimetype='application/json')

    if expenses.add_expense(content, db_params):
        return Response('{"message": "OK"}', status=200, mimetype='application/json')
    else:
        logger.error("Cannot add expense to DB")
        return Response('{"message": "Cannot add expense to DB"}', status=500, mimetype='application/json')


@app.route(ROOT_URL + '/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    if expenses.delete_expense(expense_id, db_params):
        return Response('{"message": "OK"}', status=200, mimetype='application/json')
    else:
        logger.error("Cannot delete expense from DB")
        return Response('{"message": "Cannot delete expense from DB"}', status=500, mimetype='application/json')


@app.route(ROOT_URL + '/categories', methods=['GET'])
def get_categories():
    res = expenses.get_data("categories", db_params)
    if (not res):
        logger.error("Cannot load categories from DB.\n{}".format(
            traceback.format_exc()))
        return Response('{"message": "Cannot load categories from DB"}', status=500, mimetype='application/json')
    else:
        return Response(res, status=200, mimetype='application/json')


@app.route(ROOT_URL + '/users', methods=['GET'])
def get_users():
    res = expenses.get_data("users", db_params)
    if (not res):
        logger.error("Cannot load users from DB.\n{}".format(
            traceback.format_exc()))
        return Response('{"message": "Cannot load users from DB"}', status=500, mimetype='application/json')
    else:
        return Response(res, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
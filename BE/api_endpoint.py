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
from jose import jwt
from functools import wraps
from six.moves.urllib.request import urlopen
import json
import expenses
import logging
import traceback
import sys
import os

# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all
# from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# xray_recorder.configure(service='Cash')
# plugins = ('ElasticBeanstalkPlugin', 'EC2Plugin')
# xray_recorder.configure(plugins=plugins)
# patch_all()

ROOT_URL = "/cash/v1"

# Auth0 API params
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
API_AUDIENCE = os.environ.get('API_AUDIENCE')
ALGORITHMS = ["RS256"]

app = Flask(__name__, static_url_path='/static')
CORS(app)

# Configure Flask middleware for X-Ray
# XRayMiddleware(app, xray_recorder)

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# DB params
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

# Error handling for authentication
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# Decorator to verify Access Token against auth0 JWKS
# Format error response and append status code
def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token

def requires_auth(f):
    """Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        print("Token is {}".format(token))
        url = "https://{}/.well-known/jwks.json".format(AUTH0_DOMAIN)
        jsonurl = urlopen(url)
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.route(ROOT_URL, methods=['GET'])
@requires_auth
def return_ok():
    return("OK")

#######################################################
# API endpoints
#######################################################

@app.route('/health', methods=['GET'])
def get_health():
    return Response('{"message": "healthy"}', status=200, mimetype='application/json')


@app.route(ROOT_URL + '/expenses', methods=['GET'])
#@requires_auth
def get_expenses():
    res = expenses.get_data("expenses", db_params)
    if (not res):
        logger.error("Cannot load expenses from DB.\n{}".format(
            traceback.format_exc()))
        return Response('{"message": "Cannot load expenses from DB"}', status=500, mimetype='application/json')
    else:
        return Response(res, status=200, mimetype='application/json')


@app.route(ROOT_URL + '/expenses', methods=['POST'])
#@requires_auth
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
#@requires_auth
def delete_expense(expense_id):
    if expenses.delete_expense(expense_id, db_params):
        return Response('{"message": "OK"}', status=200, mimetype='application/json')
    else:
        logger.error("Cannot delete expense from DB")
        return Response('{"message": "Cannot delete expense from DB"}', status=500, mimetype='application/json')


@app.route(ROOT_URL + '/categories', methods=['GET'])
#@requires_auth
def get_categories():
    res = expenses.get_data("categories", db_params)
    if (not res):
        logger.error("Cannot load categories from DB.\n{}".format(
            traceback.format_exc()))
        return Response('{"message": "Cannot load categories from DB"}', status=500, mimetype='application/json')
    else:
        return Response(res, status=200, mimetype='application/json')


@app.route(ROOT_URL + '/users', methods=['GET'])
#@requires_auth
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

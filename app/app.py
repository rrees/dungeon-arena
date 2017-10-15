import os
import sys
import logging

import flask
import redis

from . import handlers

ENV = os.environ.get("ENV", "PROD")

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

logger = app.logger

def setup_redis(redis_url):
    if not redis_url:
        return None
    
    return redis.from_url(redis_url, decode_responses=True)

redis = setup_redis(os.environ.get("REDIS_URL", None))

routes = [
	('/', 'index', handlers.pages.front_page, ['GET']),
	('/login/sent', 'login_sent', handlers.auth.login_sent, ['GET']),
    ('/login/problem', 'login_problem', handlers.auth.login_problem, ['GET']),
    ('/forms/login', 'login_form', handlers.auth.login_form, ['POST']),
    ('/login/<login_token>', 'auth_confirmation', handlers.auth.confirmation, ['GET']),
    ('/home', 'home', handlers.pages.home, ['GET']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
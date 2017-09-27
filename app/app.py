import os
import sys
import logging

import flask

from . import handlers

ENV = os.environ.get("ENV", "PROD")

app = flask.Flask(__name__)
app.secret_key = os.urandom(24)

logger = app.logger

routes = [
	('/', 'index', handlers.pages.front_page, ['GET']),
	('/login-sent', 'login_sent', handlers.pages.login_sent, ['GET']),
    ('/forms/login', 'login_form', handlers.auth.login_form, ['POST']),
    ('/auth/callback', 'auth_callback', handlers.auth.callback, ['GET','POST']),
    ('/home', 'home', handlers.pages.home, ['GET']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
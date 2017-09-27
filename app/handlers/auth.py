import logging
import os
import uuid

import flask
import requests

from app import app
from app.config import config

def login_form():
    email = flask.request.form.get("email")
    app.logger.info(email)

    # Generate login token
    # Save login token
    # Send email
    return flask.redirect('/login-sent')

def callback():
    code = flask.request.args.get('token')
    app.logger.info(token)
    
    # Turn token into session

    return flask.redirect(flask.url_for('home'))
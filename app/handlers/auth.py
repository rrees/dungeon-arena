import logging
import os
import uuid

import flask
import requests

from app import app
from app.config import config

from app import emails

def login_key(login_token):
    return "dungeon-arena:login:" + str(login_token)

def login_form():
    email = flask.request.form.get("email")
    app.logger.info(email)

    app.logger.info(app.redis)

    # Generate login token
    login_token = uuid.uuid4()
    app.logger.info(login_token)

    # Save login token
    app.redis.hmset(login_key(login_token), {"email": email})
    app.redis.expire(login_key(login_token), 120)

    app.logger.info(app.redis.hgetall(login_key(login_token)))

    # Send email
    emails.send_login(email, login_token)

    return flask.redirect('/login-sent')

def callback():
    code = flask.request.args.get('token')
    app.logger.info(token)

    # Check token
    
    # Turn token into session

    return flask.redirect(flask.url_for('home'))


def confirmation(login_token):
    app.logger.info(login_token)

    # Check token
    
    # Turn token into session

    return flask.redirect(flask.url_for('home'))
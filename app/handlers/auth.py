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

    app.logger.info(app.redis)

    # Generate login token
    login_token = uuid.uuid4()
    app.logger.info(login_token)
    app.redis.hmset("dungeon-arena:login:" + str(login_token), {"email": email})
    app.redis.expire(login_token, 120)

    app.logger.info(app.redis.hgetall(login_token))
    # Save login token
    # Send email
    return flask.redirect('/login-sent')

def callback():
    code = flask.request.args.get('token')
    app.logger.info(token)
    
    # Turn token into session

    return flask.redirect(flask.url_for('home'))
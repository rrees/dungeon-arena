import logging
import os
import uuid
import hashlib

import flask
import requests

from app import app
from app.config import config

from app import emails

def login_key(login_token):
    return "dungeon-arena:login:" + str(login_token)

def session_key(session_id):
    return f"dungeon-arena:session:{session_id}"

def user_key(email):
    email_hash = hashlib.md5(email).hexdigest()
    return f"dungeon-arena:user:{email_hash}"

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

def confirmation(login_token):
    app.logger.info(login_token)

    # Check token

    login_data = app.redis.hgetall(login_key(login_token))
    app.logger.info(login_data)
    app.logger.info(login_data.keys())

    if not "email" in login_data:
        app.logger.warning("Email not found in login request")
        return flask.redirect('/login')
    
    # Turn token into session
    session_id = uuid.uuid4()
    app.redis.hmset(session_key(session_id), {"email": login_data.get("email")})

    app.logger.info(session_id)

    flask.session['session_id'] = session_id
    flask.session.permanent = True

    return flask.redirect(flask.url_for('home'))
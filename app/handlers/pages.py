import logging
import os

import flask
import redis

from app.config import config

from app import app

def front_page():
	return flask.render_template('index.html')

def home():
	if not 'session_id' in flask.session:
		return flask.redirect(flask.url_for('index'))
	
	return flask.render_template('home.html')

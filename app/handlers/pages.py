import logging

import flask

from app.config import config

from app import app

def front_page():
	app.logger.info('Front page handler')
	return flask.render_template('index.html')

def home():
	return flask.render_template('home.html')

def login_sent():
	return flask.render_template('login-sent.html')
import os
import logging

import requests

from app import app

def send_login(email, login_token):

    mailgun_api_key = os.environ.get('MAILGUN_API_KEY')
    mailgun_domain = os.environ.get('MAILGUN_DOMAIN')

    url = f"https://api:{mailgun_api_key}@api.mailgun.net/v3/{mailgun_domain}"
    app.logger.info(url)

    payload = {
        'from': 'Login <login@mg.passwordless.ninja>',
        'to': email,
        'subject': 'Dungeon Arena Login',
        'text': f'http://localhost:4548/login/{login_token}'
    }
    r = requests.post(url + "/messages", data=payload)

    app.logger.info(r.status_code)

    if not r.status_code == 200:
        app.logger.warning(r.text)

import os

config = {
    "auth0": {
        "client_id": os.environ.get('AUTHO_CLIENT_ID'),
        "client_secret": os.environ.get('AUTH0_SECRET'),
        "domain": 'rrees.eu.auth0.com',
        "callback_url": {
            "DEV": "http://localhost:4548/auth/callback",
        }
    }
}
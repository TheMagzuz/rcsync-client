import jwt
import os
import configparser

_token=None


def token():
    if not _token:
        updateToken()
    return _token

def updateToken():
    global _token
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')

        token_path = os.path.expanduser(config['User']['token_path'])
        with open(token_path, 'r') as f:
            _token = f.read()
    except:
        return None
    return _token

updateToken()

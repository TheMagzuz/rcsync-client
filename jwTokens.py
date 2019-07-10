import jwt

_token=None


def token():
    if not _token:
        updateToken()
    return _token

def updateToken():
    global _token
    try:
        with open('token.dat', 'r') as f:
            _token = f.read()
    except:
        return None
    return _token

updateToken()

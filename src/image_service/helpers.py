from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature

class TokenNotValid(Exception):
    pass

def generate_token(data, exp: int) -> str:

    from setup import app

    s = Serializer(app.config['SECRET_KEY'], expires_in=exp)
    return s.dumps(data).decode('utf-8')

def check_token(token: str):

    from setup import app

    s = Serializer(app.config['SECRET_KEY'])

    try:
        data = s.loads(token)
    except (SignatureExpired, BadSignature):
        raise TokenNotValid()
    
    return data
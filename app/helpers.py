from flask import request
from functools import wraps
# from app.models import User
from os import getenv
import jwt

secretKey = getenv('SECRET_KEY')

authentication = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-CLIENT-TOKEN'
    }
}


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-CLIENT-TOKEN' in request.headers:
            token = request.headers['X-CLIENT-TOKEN']
        if not token:
            return {'errors': {'statusCode': 401,
                               'errorCode': 'E1000',
                               'message': 'Unauthorized.'}}, 401
        try:
            jwt.decode(token, secretKey)
            # currentUser = User.query.filter_by(publicId=data['sub']).first()
        except jwt.exceptions.ExpiredSignatureError:
            return {'errors': {'statusCode': 401,
                               'errorCode': 'E1002',
                               'message': 'Token is Expired.'}}, 401
        except jwt.exceptions.InvalidTokenError:
            return {'errors': {'statusCode': 401,
                               'errorCode': 'E101',
                               'message': 'Invalid Token.'
                               }}
        return f(*args, **kwargs)
    return decorated

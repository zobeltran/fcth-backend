from flask_restplus import Resource
from app.models import db, User
from app.api.models.user import api, a_auth, a_user, a_user_details
# from app.apiModels import UserSchema
from app.helpers import token_required
import jwt
from datetime import datetime, timedelta
from os import getenv
from flask_bcrypt import Bcrypt
import uuid

secretkey = getenv('SECRET_KEY')
authentication = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-CLIENT-TOKEN'
    }
}
bcrypt = Bcrypt()


@api.route('/auth/login')
class AuthenticationApi(Resource):
    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @api.expect(a_auth)
    def post(self):
        data = api.payload
        username = data['username']
        password = data['password']
        user = User.query.filter(User.username == username).first()
        if user:
            dbpassword = user.password_hashed
            checkHash = bcrypt.check_password_hash(dbpassword, password)
            role = user.role
            if checkHash:
                time = (datetime.utcnow() + timedelta(minutes=30))
                token = jwt.encode({'sub': user.publicId,
                                    'role': user.role,
                                    'exp': time,
                                    }, secretkey)
                return {'token': token.decode('utf-8'),
                        'role': role}, 200
        return {'errors': {'statusCode': 400,
                           'errorCode': 'E1004',
                           'message': 'User Not Found'}}, 400


@api.route('/register')
class RegisterApi(Resource):
        @api.doc(security=None,
                 responses={
                  200: 'Success',
                  400: 'Bad Request'
                 })
        @api.expect(a_user)
        @token_required
        def post(self):
            data = api.payload
            if data:
                passwordBycrypt = (bcrypt.
                                   generate_password_hash(data['password']))
                usernameUnique = (User.query
                                  .filter(User.username ==
                                          data['username']).all())
                if usernameUnique:
                    return {'error': {
                                      'statusCode': 400,
                                      'message': 'Username already taken'
                                      }}, 400
                else:
                    new_user = User(firstName=data['firstName'],
                                    middleName=data['middleName'],
                                    lastName=data['lastName'],
                                    username=data['username'],
                                    publicId=uuid.uuid4(),
                                    password_hashed=(passwordBycrypt
                                                     .decode('utf-8')),
                                    role=data['role'])
                    db.session.add(new_user)
                    db.session.commit()
                    return {'result': 'User has been successfull added'}, 201
            return {'error': {
                              'statusCode': 400,
                              'message': 'Please fill up the form'
                              }}, 400


@api.route('/users')
class UserApi(Resource):

    @api.doc(security='apiKey', responses={200: 'Success',
                                           401: 'Unauthorized'
                                           })
    @token_required
    @api.marshal_list_with(a_user_details, envelope='users')
    def get(self):
        view_users = User.query.all()
        return view_users, 200

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
bcrypt = Bcrypt()
errors = []


@api.route('/auth/login')
class AuthenticationApi(Resource):
    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @api.expect(a_auth)
    def post(self):
        errors.clear()
        data = api.payload
        try:
            username = data['username']
            password = data['password']
            if data:
                if not username and not password:
                    errors.append('Username must not be null')
                    errors.append('Password must not be null')
                    return {'errors': {'statuscode': 400,
                                       'errorcode': 'E1011',
                                       'message': errors}}, 400
                if not username:
                    errors.append('Username must not be null')
                    return {'errors': {'statuscode': 400,
                                       'errorcode': 'E1011',
                                       'message': errors}}, 400
                if not password:
                    errors.append('Password must not be null')
                    return {'errors': {'statuscode': 400,
                                       'errorcode': 'E1011',
                                       'message': errors}}, 400
                user = User.query.filter(User.username == username).first()
                if user:
                    dbpassword = user.password_hashed
                    checkHash = bcrypt.check_password_hash(dbpassword,
                                                           password)
                    role = user.role
                    if checkHash:
                        time = (datetime.utcnow() + timedelta(minutes=60))
                        token = jwt.encode({'sub': user.publicId,
                                            'role': user.role,
                                            'exp': time,
                                            }, secretkey)
                        return {'token': token.decode('utf-8'),
                                'role': role}, 200
                errors.append('User not found')
                return {'errors': {'statusCode': 401,
                                   'errorCode': 'E1004',
                                   'message': errors}}, 401
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400


@api.route('/register')
class RegisterApi(Resource):
        @api.doc(security=None,
                 responses={
                  200: 'Success',
                  400: 'Bad Request'
                 })
        @api.expect(a_user)
        # @token_required
        def post(self):
            try:
                errors.clear()
                data = api.payload
                firstName = data['firstName']
                middleName = data['middleName']
                email = data['email']
                lastName = data['lastName']
                username = data['username']
                password = data['password']
                publicId = uuid.uuid4()
                role = data['role']
                if data:
                    if (not firstName or
                            not middleName or
                            not lastName or
                            not username or
                            not password or
                            not email or
                            not role):
                        if not firstName:
                            errors.append('First Name must not be null')
                        if not lastName:
                            errors.append('Last Name must not be null')
                        if not username:
                            errors.append('Username must not be null')
                        if not password:
                            errors.append('Password must not be null')
                        if not email:
                            errors.append('Email must not be null')
                        if not role:
                            errors.append('Role must not be null')
                        return {'errors': {'statusCode': 400,
                                           'errorCode': 'E0002',
                                           'message': errors}}, 400
                    else:
                        passwordBycrypt = (bcrypt.
                                           generate_password_hash(password))
                        usernameUnique = (User.query
                                          .filter(User.username ==
                                                  username).all())
                        password_hashed = (passwordBycrypt.decode('utf-8'))
                        if usernameUnique:
                            errors.append('Username already taken')
                            return {'errors': {'statusCode': 400,
                                               'message': errors
                                               }}, 400
                        else:
                            new_user = User(firstName=firstName,
                                            middleName=middleName,
                                            lastName=lastName,
                                            username=username,
                                            email=email,
                                            publicId=publicId,
                                            password_hashed=password_hashed,
                                            role=role)
                            db.session.add(new_user)
                            db.session.commit()
                            return {'result':
                                    'User has been successfull added'
                                    }, 201
                    errors.append('Please fill up the form')
                    return {'errors': {
                                    'statusCode': 400,
                                    'message': errors
                                    }}, 400
            except KeyError:
                errors.append('Incomplete json nodes'),
                return {'errors': {'statusCode': 400,
                                   'errorCode': 'E0001',
                                   'message': errors
                                   }}


@api.route('')
# @cross_origin(allow_headers=['Content-Type'])
class UserApi(Resource):

    @api.doc(security='apiKey', responses={200: 'Success',
                                           401: 'Unauthorized'
                                           })
    @token_required
    @api.marshal_list_with(a_user_details, envelope='users')
    def get(self):
        view_users = User.query.all()
        return view_users, 200

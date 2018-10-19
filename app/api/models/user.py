from flask_restplus import Namespace, fields

api = Namespace('Users', 'User related APIs', path='/users')

a_user_details = api.model('users',
                           {'id': fields.Integer(),
                            'firstName': fields.String(),
                            'middleName': fields.String,
                            'lastName': fields.String(),
                            'email': fields.String(),
                            'username': fields.String(),
                            'password': fields.String(),
                            'role': fields.String(),
                            'publicId': fields.String(),
                            'dateCreated': fields.DateTime(),
                            'dateUpdated': fields.DateTime()
                            })
a_user = api.model('user',
                   {'firstName': fields.String(desc=("First Name "
                                                     "of the Employee")),
                    'middleName': fields.String(),
                    'lastName': fields.String(),
                    'email': fields.String(),
                    'username': fields.String(),
                    'password': fields.String(),
                    'role': fields.String()
                    })
a_user_schema = api.schema_model('user',
                                 {'properties': {
                                    'firstName': {
                                        'type': 'string'
                                    }
                                  },
                                  'type': 'object'
                                  })
a_auth = api.model('auth',
                   {'username': fields.String(),
                    'password': fields.String()})

from flask_restplus import Namespace, fields

api = Namespace('Users', 'User related APIs', path='/users')


a_user_name = api.model('name',
                        {'first': fields.String(desc=("First Name "
                                                      "of the Employee")),
                         'middle': fields.String(desc=("Middle Name "
                                                       "of the Employee")),
                         'last': fields.String(desc=("Last Name "
                                                     "of the Employee"))
                         })
a_user_details = api.model('users',
                           {'id': fields.Integer(),
                            'name': fields.Nested(a_user_name),
                            'email': fields.String(),
                            'username': fields.String(),
                            'passwordHashed': fields.String(),
                            'role': fields.String(),
                            'publicId': fields.String(),
                            'dateCreated': fields.DateTime(),
                            'dateUpdated': fields.DateTime()
                            })
a_user = api.model('user',
                   {'name': fields.Nested(a_user_name),
                    'email': fields.String(),
                    'username': fields.String(),
                    'password': fields.String(),
                    'role': fields.String()
                    })
a_auth = api.model('auth',
                   {'username': fields.String(),
                    'password': fields.String()})

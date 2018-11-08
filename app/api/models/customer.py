from flask_restplus import Namespace, fields

api = Namespace('Customer', 'Customer Related APIs', path='/customer')

customerDetails = api.model('Customer Details',
                            {'id': fields.Integer(),
                             'firstName': fields.String(),
                             'lastName': fields.String(),
                             'email': fields.String(),
                             'contactNo': fields.String(),
                             'isArchived': fields.Boolean()})

postCustomer = api.model('Post Customer',
                         {'requestId': fields.Integer(),
                          'firstName': fields.String(),
                          'lastName': fields.String(),
                          'email': fields.String(),
                          'contactNo': fields.String()})

deleteCustomer = api.model('Delete Customer',
                           {'isArchived': fields.Boolean()})

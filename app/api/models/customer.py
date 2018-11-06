from flask_restplus import Namespace, fields

api = Namespace('Customer', 'Customer Related APIs', path='/customer')

customerDetails = api.model('Customer Details',
                            {'id': fields.Integer(),
                             'firstName': fields.String(),
                             'lastName': fields.String(),
                             'email': fields.String(),
                             'contactNumber': fields.String(),
                             'isArchived': fields.Boolean()})

postCustomer = api.model('Post Customer',
                         {'firstName': fields.String(),
                          'lastName': fields.String(),
                          'email': fields.String(),
                          'contactNumber': fields.String()})

deleteCustomer = api.model('Delete Customer',
                           {'isArchived': fields.Boolean()})

from flask_restplus import Namespace, fields

api = Namespace('Packages', 'Packages Related APIs', path='/packages')

packageDetails = api.model('Package Details',
                           {'id': fields.Integer(),
                            'destination': fields.String(),
                            'price': fields.Float(),
                            'days': fields.Integer(),
                            'itenerary': fields.String(),
                            'inclusions': fields.Stirng(),
                            'remainingSlots': fields.String(),
                            'expirationDate': fields.Date(),
                            'note': fields.String(),
                            'hotel': fields.Integer(),
                            'flight': fields.Integer(),
                            'isExpired': fields.Boolean()
                            })
postPackage = api.model('Post Package',
                        {
                         'destination': fields.String(),
                         'price': fields.Float(),
                         'days': fields.Integer(),
                         'itenerary': fields.String(),
                         'inclusions': fields.String(),
                         'remainingSlots': fields.String(),
                         'expirationDate': fields.Date(),
                         'note': fields.String(),
                         'hotel': fields.Integer(),
                         'flight': fields.Integer(),
                         'isExpired': fields.Boolean()
                         })
deletePackage = api.model('Delete Package',
                          {'isArchived': fields.Boolean()})

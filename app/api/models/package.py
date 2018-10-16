from flask_restplus import Namespace, fields

api = Namespace('Packages', 'Packages Related APIs', path='/packages')

packageDetails = api.model('packages',
                           {'id': fields.Integer(),
                            'destination': fields.String(),
                            'price': fields.Decimal(),
                            'days': fields.Integer(),
                            'intenerary': fields.String(),
                            'inclusions': fields.String(),
                            'remainingSlots': fields.Integer(),
                            'expirationDate': fields.Date(),
                            'note': fields.String(),
                            'hotel': fields.String(),
                            'flight': fields.String(),
                            'isExpired': fields.Boolean()
                            })

packageInsert = api.model('packages',
                          {'destination': fields.String(),
                           'price': fields.Decimal(),
                           'days': fields.Integer(),
                           'intenerary': fields.String(),
                           'inclusions': fields.String(),
                           'remainingSlots': fields.Integer(),
                           'expirationDate': fields.Date(),
                           'note': fields.String(),
                           'hotel': fields.String(),
                           'flight': fields.String(),
                           'isExpired': fields.Boolean()
                           })

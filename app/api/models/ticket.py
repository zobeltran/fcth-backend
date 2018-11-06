from flask_restplus import Namespace, fields

api = Namespace('Flights', 'Flight Related APIs', path='/flights')

flightDetails = api.model('flights',
                          {'id': fields.Integer(),
                           'flightNo': fields.String(),
                           'origin': fields.String(),
                           'arrival': fields.String(),
                           'departureDate': fields.Date(),
                           'departureTime': fields.String(),
                           'returnDate': fields.Date(),
                           'returnTime': fields.String(),
                           'remainingSlots': fields.String(),
                           'expirationDate': fields.String(),
                           'price': fields.Float(),
                           'isExpired': fields.Boolean(),
                           'isPackaged': fields.Boolean(),
                           'dateCreated': fields.DateTime(),
                           'dateUpdated': fields.DateTime()
                           })
postFlight = api.model('Post Fights',
                       {'flightNo': fields.String(),
                        'origin': fields.String(),
                        'arrival': fields.String(),
                        'departureDate': fields.Date(),
                        'departureTime': fields.String(),
                        'returnDate': fields.Date(),
                        'returnTime': fields.String(),
                        'remainingSlots': fields.String(),
                        'expirationDate': fields.String(),
                        'price': fields.Float(),
                        'isExpired': fields.Boolean(),
                        'isPackaged': fields.Boolean()
                        })
deleteFlight = api.model('Delete Flight', {'isArchived': fields.Boolean()})

from flask_restplus import Namespace, fields

api = Namespace('Hotels', 'Hotels Related APIs', path='/hotels')

hotelDetails = api.model('Hotel Details',
                         {'id': fields.Integer(),
                          'name': fields.String(),
                          'roomType': fields.String(),
                          'capacity': fields.String(),
                          'details': fields.String(),
                          'checkIn': fields.DateTime(),
                          'checkOut': fields.DateTime(),
                          'price': fields.Float(),
                          'expirationDate': fields.Date(),
                          'isExpired': fields.Boolean(),
                          'isPackaged': fields.Boolean(),
                          'remainingRooms': fields.Integer(),
                          'dateCreated': fields.DateTime(),
                          'dateUpdated': fields.DateTime()})

postHotel = api.model('Post Hotels',
                      {'name': fields.String(),
                       'roomType': fields.String(),
                       'capacity': fields.String(),
                       'details': fields.String(),
                       'checkIn': fields.DateTime(),
                       'checkOut': fields.DateTime(),
                       'price': fields.Float(),
                       'expirationDate': fields.Date(),
                       'isExpired': fields.Boolean(),
                       'isPackaged': fields.Boolean(),
                       'remainingRooms': fields.Integer()})

deleteHotel = api.model('Delete Model',
                        {'isArchived': fields.Boolean()})

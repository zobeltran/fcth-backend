from flask_restful import Namespace, fields

api = Namespace('Bookings', 'Booking Related APIs', path='/bookings')

flightBookingDetails = api.model('Flight Booking Details',
                                 {'id': fields.Integer(),
                                  'referenceNumber': fields.String(),
                                  'customer': fields.Integer(),
                                  'flight': fields.Integer(),
                                  'isPaid': fields.Boolean()})

hotelBookingDetails = api.model('Hotel Booking Details',
                                {'id': fields.Integer(),
                                 'referenceNumber': fields.String(),
                                 'customer': fields.Integer(),
                                 'hotel': fields.Integer(),
                                 'isPaid': fields.Boolean()})

packageBookingDetails = api.model('Package Booking Details',
                                  {'id': fields.Integer(),
                                   'referenceNumber': fields.String(),
                                   'customer': fields.Integer(),
                                   'package': fields.Integer(),
                                   'isPaid': fields.Boolean()})

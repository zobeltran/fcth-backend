from flask_restplus import Namespace, fields

api = Namespace('Inquiries', 'Inquiries Related APIs', path='/inquiries')

flightInquiryDetails = api.model('Flight Inquiries',
                                 {'id': fields.Integer(),
                                  'firstName': fields.String(),
                                  'lastName': fields.String(),
                                  'email': fields.String(),
                                  'origin': fields.Stirng(),
                                  'arrival': fields.String(),
                                  'departureDate': fields.Date(),
                                  'arrivalDate': fields.Date(),
                                  'time': fields.String(),
                                  'adult': fields.Integer(),
                                  'child': fields.Integer(),
                                  'infant': fields.Integer(),
                                  'note': fields.String()
                                  })

hotelInquiriesDetails = api.model('Hotel Inquiries',
                                  {'id': fields.Integer(),
                                   'firstName': fields.String(),
                                   'lastName': fields.String(),
                                   'email': fields.String(),
                                   'location': fields.String(),
                                   'budget': fields.Float(),
                                   'guest': fields.Integer(),
                                   'checkIn': fields.Date(),
                                   'checkOut': fields.Date(),
                                   'note': fields.String()})

postFlightInquiries = api.model('Post Flight Inquiries',
                                {'firstName': fields.String(),
                                 'lastName': fields.String(),
                                 'email': fields.String(),
                                 'origin': fields.Stirng(),
                                 'arrival': fields.String(),
                                 'departureDate': fields.Date(),
                                 'arrivalDate': fields.Date(),
                                 'time': fields.String(),
                                 'adult': fields.Integer(),
                                 'child': fields.Integer(),
                                 'infant': fields.Integer(),
                                 'note': fields.String()})

postHotelInquies = api.model('Post Hotel Inquiries',
                             {'firstName': fields.String(),
                              'lastName': fields.String(),
                              'email': fields.String(),
                              'location': fields.String(),
                              'budget': fields.Float(),
                              'guest': fields.Integer(),
                              'checkIn': fields.Date(),
                              'checkOut': fields.Date(),
                              'note': fields.String()})

deleteFlightInquiries = api.model('Delete Flight Inquiry',
                                  {'isArchived': fields.Boolean()})

deleteHotelInquries = api.model('Delete Hotel Inquiry',
                                {'isArchived': fields.Boolean()})

from flask_restplus import Namespace, fields

api = Namespace('Flights', 'Flight Related APIs', path='/flights')

flightDetails = api.model('flights',
                          {'id': fields.Integer(),
                           'flightNo': fields.String})
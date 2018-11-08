from flask_restplus import Resource
from app.models import db, PackageBooking, HotelBooking, FlightBooking
from app.helpers import token_required
from app.api.models.bookings import api, flightBookingDetails
from app.api.models.bookings import hotelBookingDetails, packageBookingDetails
from datetime import datetime
from dateutil.parser import parse

errors = []
now = datetime.now()


@api.route('/flight')
class FlightBookingsApi(Resource):
    @api.doc(security=None,
             response={
                200: 'Success',
                400: 'Bad Request'
             })
    @api.marshal_list_with(flightBookingDetails,
                           envelope='FlightBookingDetails')
    @token_required
    def get(self):
        viewFlightBookings = FlightBooking.query.all()
        return viewFlightBookings, 200


@api.route('/hotel')
class HotelBookingApi(Resource):
    @api.doc(security=None,
             response={
                 200: 'Success',
                 400: 'Bad Request'
             })
    @token_required
    @api.marshal_list_with(hotelBookingDetails,
                           envelope='HotelBookingDetails')
    def get(self):
        viewHotelBookings = HotelBooking.query.all()
        return viewHotelBookings, 200


@api.route('/package')
class PackageBookingApi(Resource):
    @api.doc(security=None,
             response={
                 200: 'Success',
                 400: 'Bad Request'
             })
    @token_required
    @api.marshal_list_with(packageBookingDetails,
                           envelope='PackageBookingDetails')
    def get(self):
        viewPackageBookings = PackageBooking.query.all()
        return viewPackageBookings, 200

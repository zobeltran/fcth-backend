from flask_restplus import Resource
from app.models import db, Hotel
from app.helpers import token_required
from app.api.models.hotel import api, hotelDetails, postHotel, deleteHotel
from datetime import datetime
from dateutil.parser import parse

errors = []
now = datetime.now()


@api.route('')
class HotelApi(Resource):
    @api.doc(security='apiKey',
             responses={
                200: 'Success',
                400: 'Bad Request'
             })
    @token_required
    @api.marshal_with(hotelDetails, envelope='hotels')
    def get(self):
        views_hotels = (Hotel.query.filter(Hotel.isArchived.is_(False))
                        .filter(Hotel.isPackaged.is_(False)).all())
        return views_hotels, 200

    @api.doc(security='apiKey',
             responses={
                200: 'Success',
                400: 'Bad Request'
             })
    @token_required
    @api.expect(postHotel)
    def post(self):
        errors.clear()
        data = api.payload
        try:
            name = data['name']
            roomType = data['roomType']
            capacity = data['capacity']
            details = data['details']
            checkIn = parse(data['checkIn'])
            print(checkIn)
            print(now)
            print(type(checkIn))
            checkOut = parse(data['checkOut'])
            price = float(data['price'])
            expirationDate = parse(data['expirationDate'])
            isExpired = data['isExpired']
            isPackaged = data['isPackaged']
            remainingRooms = data['remainingRooms']
            if (not name or not roomType
                    or not capacity
                    or not details
                    or not checkIn
                    or not checkOut
                    or not price
                    or not expirationDate
                    or not remainingRooms):
                if not name:
                    errors.append('Name must not be null')
                if not roomType:
                    errors.append('Room Type must not be null')
                if not capacity:
                    errors.append('Capacity must not be null')
                if not details:
                    errors.append('Details must not be null')
                if not price:
                    errors.append('Price must not be null')
                if not expirationDate:
                    errors.append('Expiration date must not be null')
                if not remainingRooms:
                    errors.append('Remaining Room must not be null')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            elif (checkIn <= now or checkOut <= now
                    or checkOut <= checkIn
                    or expirationDate <= now
                    or expirationDate > checkIn
                    or price <= 0
                    or remainingRooms <= 0):
                if checkIn <= now:
                    errors.append('Check In date must be greater than '
                                  'the date today')
                if checkOut <= now:
                    errors.append('Check Out date must be greater than '
                                  'the date today')
                if checkOut <= checkIn:
                    errors.append('Check out date must not be less than '
                                  'Check in date')
                if expirationDate <= now:
                    errors.append('Expiration date must be greater than '
                                  'the date today')
                if expirationDate > checkIn:
                    errors.append('Expiration date must be less than the '
                                  'the check In date')
                if price <= 0:
                    errors.append('Price must be greater than zero')
                if remainingRooms <= 0:
                    errors.append('Remaining rooms must be greater '
                                  'than zero')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3001',
                                   'message': errors}}, 400
            else:
                new_hotel = Hotel(name=name,
                                  roomType=roomType,
                                  capacity=capacity,
                                  details=details,
                                  checkIn=checkIn,
                                  checkOut=checkOut,
                                  price=price,
                                  expirationDate=expirationDate,
                                  remainingRooms=remainingRooms,
                                  isExpired=isExpired,
                                  isPackaged=isPackaged)
                db.session.add(new_hotel)
                db.session.commit()
                return {'message': 'Successful added a new hotel'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400


@api.route('/id=<int:id>')
@api.response(404, 'Not Found')
@api.param('id', 'Hotel Id')
class HotelIdApi(Resource):
    @api.doc(security='apiKey',
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    @api.marshal_list_with(hotelDetails, envelope='hotelDetails')
    def get(self, id):
        viewHotel = (Hotel.query.filter(Hotel.isArchived.is_(False))
                     .filter(Hotel.id == id).all())
        return viewHotel, 200

    @api.doc(security='apiKey',
             response={
                 200: 'Success',
                 400: 'Bad Request'
             })
    @token_required
    @api.expect(postHotel)
    def put(self, id):
        errors.clear()
        data = api.payload
        try:
            name = data['name']
            roomType = data['roomType']
            capacity = data['capacity']
            details = data['details']
            checkIn = parse(data['checkIn'])
            checkOut = parse(data['checkOut'])
            price = data['price']
            expirationDate = parse(data['expirationDate'])
            isExpired = data['isExpired']
            isPackaged = data['isPackaged']
            remainingRooms = data['remainingRooms']
            if (not name or not roomType
                    or not capacity
                    or not details
                    or not checkIn
                    or not checkOut
                    or not price
                    or not expirationDate
                    or not remainingRooms):
                if not name:
                    errors.append('Name must not be null')
                if not roomType:
                    errors.append('Room Type must not be null')
                if not capacity:
                    errors.append('Capacity must not be null')
                if not details:
                    errors.append('Details must not be null')
                if not price:
                    errors.append('Price must not be null')
                if not expirationDate:
                    errors.append('Expiration date must not be null')
                if not remainingRooms:
                    errors.append('Remaining Room must not be null')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            elif (checkIn <= now or checkOut <= now
                    or checkOut <= checkIn
                    or expirationDate <= now
                    or expirationDate > checkIn
                    or price <= 0
                    or remainingRooms <= 0):
                if checkIn <= now:
                    errors.append('Check In date must be greater than '
                                  'the date today')
                if checkOut <= now:
                    errors.append('Check Out date must be greater than '
                                  'the date today')
                if checkOut <= checkIn:
                    errors.append('Check out date must not be less than '
                                  'Check in date')
                if expirationDate <= now:
                    errors.append('Expiration date must be greater than '
                                  'the date today')
                if expirationDate > checkIn:
                    errors.append('Expiration date must be less than the '
                                  'the check In date')
                if price <= 0:
                    errors.append('Price must be greater than zero')
                if remainingRooms <= 0:
                    errors.append('Remaining rooms must be greater '
                                  'than zero')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3001',
                                   'message': errors}}, 400
            else:
                Hotel.name = name,
                Hotel.roomType = roomType,
                Hotel.capacity = capacity,
                Hotel.details = details,
                Hotel.checkIn = checkIn,
                Hotel.checkOut = checkOut,
                Hotel.price = price,
                Hotel.expirationDate = expirationDate,
                Hotel.remainingRooms = remainingRooms,
                Hotel.isExpired = isExpired,
                Hotel.isPackaged = isPackaged
                db.session.commit()
                return {'message': 'Successfully updated'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400

    @api.doc(security='apiKey',
             response={
                 200: 'Success',
                 400: 'Bad Request'
             })
    @token_required
    @api.expect(deleteHotel)
    def delete(self, id):
        errors.clear()
        hotel = Hotel.query.get(id)
        data = api.payload
        try:
            if not hotel:
                errors.append('Id does not exist')
                return {'errors': {'status': 400,
                                   'errorCode': 'E0001',
                                   'message': errors}}, 400
            else:
                hotel.isArchived = data['isArchived']
                db.session.commit()
                return {'message': 'Successfully Deleted'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400

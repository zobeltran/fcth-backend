from flask_restplus import Resource
from app.models import db, Ticket
from app.api.models.ticket import api, flightDetails, postFlight, deleteFlight
from app.helpers import token_required
from datetime import datetime
from dateutil.parser import parse

errors = []
now = datetime.now()


@api.route('')
class TicketApi(Resource):
    @api.doc(security='apiKey',
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @api.marshal_list_with(flightDetails, envelope='flights')
    def get(self):
        viewFlights = (Ticket.query.filter(Ticket.isArchived.is_(False))
                       .filter(Ticket.isPackaged.is_(False)).all())
        return viewFlights, 200

    @api.doc(security='apiKey',
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    @api.expect(postFlight)
    def post(self):
        errors.clear()
        data = api.payload
        try:
            flightNo = data['flightNo']
            origin = data['origin']
            arrival = data['arrival']
            departureDate = parse(data['departureDate'])
            departureTime = parse(data['departureTime'])
            returnDate = parse(data['returnDate'])
            returnTime = data['returnTime']
            remainingSlots = int(data['remainingSlots'])
            expirationDate = parse(data['expirationDate'])
            price = float(data['price'])
            isExpired = data['isExpired']
            isPackaged = data['isPackaged']
            if (not flightNo or not origin or not arrival
                    or not departureDate or not departureTime
                    or not returnDate or not returnTime
                    or not remainingSlots or not price
                    or not expirationDate):
                if not flightNo:
                    errors.append('Flight Number must not be null')
                if not origin:
                    errors.append('Origin must no be null')
                if not arrival:
                    errors.append('Arrival must not be null')
                if not departureDate:
                    errors.append('Departure date must not be null')
                if not departureTime:
                    errors.append('Departure Time must not be null')
                if not returnDate:
                    errors.append('Return date must not be null')
                if not returnTime:
                    errors.append('Return time must not be null')
                if not remainingSlots:
                    errors.append('Remaining slots must not be null')
                if not price:
                    errors.append('Price must not be null')
                if not expirationDate:
                    errors.append('Expiration date must not be null')
                return {'errors': {'status': 400,
                                   'errorCode': 'E2000',
                                   'message': errors}}, 400
            elif (departureDate <= now or returnDate <= now
                    or returnDate <= departureDate
                    or remainingSlots <= 0
                    or expirationDate <= now
                    or price <= 0
                    or expirationDate >= departureDate):
                if departureDate <= now:
                    errors.append('Departure date must not be less or '
                                  'equal to today\'s date')
                if returnDate <= now:
                    errors.append('Return date must not be less or '
                                  'equal to today\'s date')
                if returnDate <= departureDate:
                    errors.append('Return date must not be less or '
                                  'equal to departure date')
                if remainingSlots <= 0:
                    errors.append('Remaining Slots must be greater '
                                  'than zero')
                if price <= 0:
                    errors.append('Price must be greater than zero')
                if expirationDate <= now:
                    errors.append('Expiration date must not be less or '
                                  'equal to today\'s date')
                if expirationDate >= departureDate:
                    errors.append('Expiration date must not be greater or '
                                  'equal to departure date')
                return {'errors': {'status': 400,
                                   'errorCode': 'E2001',
                                   'message': errors}}, 400
            else:
                new_ticket = Ticket(flightNo=flightNo,
                                    origin=origin,
                                    arrival=arrival,
                                    departureDate=departureDate,
                                    departureTime=departureTime,
                                    returnDate=returnDate,
                                    returnTime=returnTime,
                                    remainingSlots=remainingSlots,
                                    price=price,
                                    expirationDate=expirationDate,
                                    isExpired=isExpired,
                                    isPackaged=isPackaged
                                    )
                db.session.add(new_ticket)
                db.session.commit()
                return {'message': 'Successfully added a new ticket'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400


@api.route('/id=<int:id>')
@api.response(404, 'Not Found')
@api.param('id', 'Flight Id')
class TicketIdApi(Resource):
    @api.doc(security='apiKey',
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    @api.marshal_list_with(flightDetails, envelope='flightDetails')
    def get(self, id):
        viewFlights = (Ticket.query.filter(Ticket.isArchived.is_(False))
                       .filter(Ticket.id == id).all())
        return viewFlights, 200

    @api.doc(security='apiKey',
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    @api.expect(postFlight)
    def put(self, id):
        errors.clear()
        data = api.payload
        try:
            flightNo = data['flightNo']
            origin = data['origin']
            arrival = data['arrival']
            departureDate = parse(data['departureDate'])
            departureTime = parse(data['departureTime'])
            returnDate = parse(data['returnDate'])
            returnTime = data['returnTime']
            remainingSlots = int(data['remainingSlots'])
            expirationDate = parse(data['expirationDate'])
            price = float(data['price'])
            isExpired = data['isExpired']
            isPackaged = data['isPackaged']
            if (not flightNo or not origin or not arrival
                    or not departureDate or not departureTime
                    or not returnDate or not returnTime
                    or not remainingSlots or not price
                    or not expirationDate):
                if not flightNo:
                    errors.append('Flight Number must not be null')
                if not origin:
                    errors.append('Origin must no be null')
                if not arrival:
                    errors.append('Arrival must not be null')
                if not departureDate:
                    errors.append('Departure date must not be null')
                if not departureTime:
                    errors.append('Departure Time must not be null')
                if not returnDate:
                    errors.append('Return date must not be null')
                if not returnTime:
                    errors.append('Return time must not be null')
                if not remainingSlots:
                    errors.append('Remaining slots must not be null')
                if not price:
                    errors.append('Price must not be null')
                if not expirationDate:
                    errors.append('Expiration date must not be null')
                return {'errors': {'status': 400,
                                   'errorCode': 'E2000',
                                   'message': errors}}, 400
            elif (departureDate <= now or returnDate <= now
                    or returnDate <= departureDate
                    or remainingSlots <= 0
                    or expirationDate <= now
                    or price <= 0
                    or expirationDate >= departureDate):
                if departureDate <= now:
                    errors.append('Departure date must not be less or '
                                  'equal to today\'s date')
                if returnDate <= now:
                    errors.append('Return date must not be less or '
                                  'equal to today\'s date')
                if returnDate <= departureDate:
                    errors.append('Return date must not be less or '
                                  'equal to departure date')
                if remainingSlots <= 0:
                    errors.append('Remaining Slots must be greater '
                                  'than zero')
                if price <= 0:
                    errors.append('Price must be greater than zero')
                if expirationDate <= now:
                    errors.append('Expiration date must not be less or '
                                  'equal to today\'s date')
                if expirationDate >= departureDate:
                    errors.append('Expiration date must not be greater or '
                                  'equal to departure date')
                return {'errors': {'status': 400,
                                   'errorCode': 'E2001',
                                   'message': errors}}, 400
            else:
                ticket = Ticket.query.get(id)
                if not ticket:
                    errors.append('Id not existing')
                    return {'errors': {'status': 400,
                                       'errorCode': 'E2002',
                                       'message': errors}}, 400
                else:
                    ticket.flightNo = flightNo
                    ticket.origin = origin
                    ticket.arrival = arrival
                    ticket.departureDate = departureDate
                    ticket.departureTime = departureTime
                    ticket.returnDate = returnDate
                    ticket.returnTime = returnTime
                    ticket.remainingSlots = remainingSlots
                    ticket.price = price
                    ticket.expirationDate = expirationDate
                    ticket.isExpired = isExpired
                    ticket.isPackaged = isPackaged
                    db.session.commit()
                    return {'message': 'Successfully updated'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400

    @api.doc(security='apiKey')
    @token_required
    @api.expect(deleteFlight)
    def delete(self, id):
        errors.clear()
        ticket = Ticket.query.get(id)
        data = api.payload
        try:
            if not ticket:
                errors.append('Id does not exist')
                return {'errors': {'status': 400,
                                   'errorCode': 'E0001',
                                   'message': errors}}, 400
            else:
                ticket.isArchived = data['isArchived']
                db.session.commit()
                return {'message': 'Successfully Deleted'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400

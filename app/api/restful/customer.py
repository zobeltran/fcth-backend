from flask_restplus import Resource
from app.api.models.customer import api, customerDetails, postCustomer
from app.models import db, Customer, PackageBooking, HotelBooking
from app.models import FlightBooking
from datetime import datetime

referenceNumber = datetime.now().strftime("%Y%m%d%H%M%S")
errors = []


@api.route('')
class CustomerApi(Resource):
    @api.doc(security=None,
             responses={
                200: 'Success',
                400: 'Bad Request'
             })
    # @token_required
    @api.marshal_with(customerDetails, envelope='customer')
    def get(self):
        view_customer = (Customer.query.filter(Customer.isArchived.is_(False))
                         .all())
        return view_customer, 200


@api.route('/id=<int:id>')
@api.response(404, 'Not Found')
@api.param('id', 'Customer Id')
class CustomerIdApi(Resource):
    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    # @token_required
    # @api.marshal_list_with(customerDetails, envelope='customerDetails')
    def get(self, id):
        view_customer = (Customer.query
                         .filter(Customer.id == id).first())
        if not view_customer:
            errors.append('Id does not exist')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400
        else:
            return api.marshal(view_customer, customerDetails,
                               envelope='customerDetails'), 200


@api.route('/packageCustomer')
class CustomerPackageApi(Resource):
    @api.doc(security=None,
             responses={
                200: 'Success',
                400: 'Bad Request'
             })
    @api.expect(postCustomer)
    def post(self):
        errors.clear()
        data = api.payload
        try:
            packageId = data['requestId']
            firstName = data['firstName']
            lastName = data['lastName']
            email = data['email']
            contactNo = data['contactNo']
            if(not firstName or not lastName
                    or not email or not contactNo):
                if not firstName:
                    errors.append('First Name is Required')
                if not lastName:
                    errors.append('Last Name is Required')
                if not email:
                    errors.append('Email is Required')
                if not contactNo:
                    errors.append('Contact Number is Required')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            else:
                new_customer = Customer(firstName=firstName,
                                        lastName=lastName,
                                        email=email,
                                        contactNo=contactNo)
                db.session.add(new_customer)
                db.session.commit()
                packageTransaction = PackageBooking(
                                        referenceNumber="PB"+referenceNumber,
                                        customer=new_customer.id,
                                        package=packageId
                                        )
                db.session.add(packageTransaction)
                db.session.commit()
                return {'message': 'Successful Booking',
                        'bookingId': packageTransaction.id}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400


@api.route('/hotelCustomer')
class CustomerHotelApi(Resource):
    @api.doc(security=None,
             responses={
                200: 'Success',
                400: 'Bad Request'
             })
    @api.expect(postCustomer)
    def post(self):
        errors.clear()
        data = api.payload
        try:
            hotelId = data['requestId']
            firstName = data['firstName']
            lastName = data['lastName']
            email = data['email']
            contactNo = data['contactNo']
            if(not firstName or not lastName
                    or not email or not contactNo):
                if not firstName:
                    errors.append('First Name is Required')
                if not lastName:
                    errors.append('Last Name is Required')
                if not email:
                    errors.append('Email is Required')
                if not contactNo:
                    errors.append('Contact Number is Required')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            else:
                new_customer = Customer(firstName=firstName,
                                        lastName=lastName,
                                        email=email,
                                        contactNo=contactNo)
                db.session.add(new_customer)
                db.session.commit()
                hotelTransaction = HotelBooking(
                                    referenceNumber='HB'+referenceNumber,
                                    customer=new_customer.id,
                                    flight=hotelId
                                    )
                db.session.add(hotelTransaction)
                db.session.commit()
                return {'message': 'Successful Booking',
                        'bookingId': hotelTransaction.id}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400


@api.route('/flightCustomer')
class CustomerFlightApi(Resource):
    @api.doc(security=None,
             responses={
                200: 'Success',
                400: 'Bad Request'
             })
    @api.expect(postCustomer)
    def post(self):
        errors.clear()
        data = api.payload
        try:
            flightId = data['requestId']
            firstName = data['firstName']
            lastName = data['lastName']
            email = data['email']
            contactNo = data['contactNo']
            if(not firstName or not lastName
                    or not email or not contactNo):
                if not firstName:
                    errors.append('First Name is Required')
                if not lastName:
                    errors.append('Last Name is Required')
                if not email:
                    errors.append('Email is Required')
                if not contactNo:
                    errors.append('Contact Number is Required')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            else:
                new_customer = Customer(firstName=firstName,
                                        lastName=lastName,
                                        email=email,
                                        contactNo=contactNo)
                db.session.add(new_customer)
                db.session.commit()
                flightTransaction = FlightBooking(
                                        referenceNumber='FB'+referenceNumber,
                                        customer=new_customer.id,
                                        flight=flightId
                                        )
                db.session.add(flightTransaction)
                db.session.commit()
                return {'message': 'Successful Booking',
                        'bookingId': flightTransaction.id}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400

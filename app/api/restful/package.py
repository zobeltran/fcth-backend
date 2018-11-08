from flask_restplus import Resource
from app.models import db, Package
from app.api.models.packages import api, packageDetails, postPackage
from app.helpers import token_required
from datetime import datetime
from dateutil.parser import parse

errors = []
now = datetime.now()


@api.route('')
# @cross_origin(allow_headers=['Content-Type'])
class PackagesApi(Resource):
    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @api.marshal_list_with(packageDetails, envelope='packages')
    def get(self):
        viewPackages = Package.query.all()
        return viewPackages

    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    @api.expect(postPackage)
    def post(self):
        errors.clear()
        data = api.payload
        destination = data['destination']
        price = float(data['price'])
        days = int(data['days'])
        intenerary = data['itenerary']
        inclusions = data['inclusions']
        remainingSlots = data['remainingSlots']
        expirationDate = parse(data['expirationDate'])
        note = data['note']
        hotel = int(data['hotel'])
        flight = int(data['flight'])
        isExpired = data['isExpired']
        try:
            if (not destination or not price or not days
                    or not intenerary or not inclusions
                    or not remainingSlots or not expirationDate
                    or not note or not hotel or not flight):
                if not destination:
                    errors.append('Please add a destination')
                if not price:
                    errors.append('Please add a price')
                if not inclusions:
                    errors.append('Please add an inclusions')
                if not remainingSlots:
                    errors.append('Please add a remaining slot')
                if not note:
                    errors.append('Please add a note')
                if not expirationDate:
                    errors.append('Please add a Expiration Date')
                if not hotel:
                    errors.append('Please add a Hotel')
                if not flight:
                    errors.append('Please add a flight')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            else:
                newPackage = Package(destination=destination,
                                     price=price,
                                     days=days,
                                     intenerary=intenerary,
                                     inclusions=inclusions,
                                     remainingSlots=remainingSlots,
                                     expirationDate=expirationDate,
                                     note=note,
                                     hotel=hotel,
                                     flight=flight,
                                     isExpired=isExpired)
                db.session.add(newPackage)
                db.session.commit()
                return {'result': 'Package has been successfull added'}, 201
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400


@api.route('?id=<int:id>')
@api.response(404, 'Not Found')
# @cross_origin(allow_headers=['Content-Type'])
@api.param('id', 'Package Id')
class PackageIdApi(Resource):
    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    @api.expect(postPackage)
    # @cross_origin(allow_headers=['Content-Type'])
    def put(self):
        errors.clear()
        data = api.payload
        destination = data['destination']
        price = float(data['price'])
        days = int(data['days'])
        intenerary = data['itenerary']
        inclusions = data['inclusions']
        remainingSlots = data['remainingSlots']
        expirationDate = parse(data['expirationDate'])
        note = data['note']
        hotel = int(data['hotel'])
        flight = int(data['flight'])
        isExpired = data['isExpired']
        try:
            if (not destination or not price or not days
                    or not intenerary or not inclusions
                    or not remainingSlots or not expirationDate
                    or not note or not hotel or not flight):
                if not destination:
                    errors.append('Please add a destination')
                if not price:
                    errors.append('Please add a price')
                if not inclusions:
                    errors.append('Please add an inclusions')
                if not remainingSlots:
                    errors.append('Please add a remaining slot')
                if not note:
                    errors.append('Please add a note')
                if not expirationDate:
                    errors.append('Please add a Expiration Date')
                if not hotel:
                    errors.append('Please add a Hotel')
                if not flight:
                    errors.append('Please add a flight')
                return {'errors': {'status': 400,
                                   'errorCode': 'E3000',
                                   'message': errors}}, 400
            else:
                package = Package.query.get(id)
                if not package:
                    errors.append('Id not existing')
                    return {'errors': {'status': 400,
                                       'errorCode': 'E2002',
                                       'message': errors}}, 400
                else:
                    package.destination = destination,
                    package.price = price,
                    package.days = days,
                    package.intenerary = intenerary,
                    package.inclusions = inclusions,
                    package.remainingSlots = remainingSlots,
                    package.expirationDate = expirationDate,
                    package.note = note,
                    package.hotel = hotel,
                    package.flight = flight,
                    package.isExpired = isExpired
                    db.session.commit()
                    return {'result': 'Successfully updated'}, 200
        except KeyError:
            errors.append('Incomplete json nodes')
            return {'errors': {'status': 400,
                               'errorCode': 'E0001',
                               'message': errors}}, 400

    @api.doc(security=None,
             responses={
              200: 'Success',
              400: 'Bad Request'
             })
    @token_required
    # @api.expect(postPackage)
    # @cross_origin(allow_headers=['Content-Type'])
    def delete(self):
        return {'result': 'Package has been deleted'}

from flask_restplus import Resource
from app.models import db, Package
from app.api.models.packages import api, packageDetails, postPackage
from app.helpers import token_required


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
        data = api.payload
        if data:
            newPackage = Package(destination=data['destination'],
                                 price=data['price'],
                                 days=data['days'],
                                 intenerary=data['itenerary'],
                                 inclusions=data['inclusions'],
                                 remainingSlots=data['remainingSlots'],
                                 expirationDate=data['expirationDate'],
                                 note=data['note'],
                                 hotel=data['hotel'],
                                 flight=data['flight'],
                                 isExpired=data['isExpired']
                                 )
            db.session.add(newPackage)
            db.session.commit()
            return {'result': 'Package has been successfull added'}, 201
        return {'error': {'statusCode': 400,
                          'errorCode': 'E2000',
                          'message': 'Please fill up the form'
                          }}, 400


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
        data = api.payload
        if data:
            Package.destination = data['destination']
            Package.price = data['price']
            Package.days = data['days']
            Package.intenerary = data['itenerary']
            Package.inclusions = data['inclusions']
            Package.remainingSlots = data['remainingSlots']
            Package.expirationDate = data['expirationDate']
            Package.note = data['note']
            Package.hotel = data['hotel']
            Package.flight = data['flight']
            Package.isExpired = data['isExpired']
            db.session.commit()
            return {'result': 'Package has been updated'}, 200
        return {'error': {'statusCode': 400,
                          'errorCode': 'E2000',
                          'message': 'Please fill up the form'}}, 400

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

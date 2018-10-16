from flask_restplus import Resource
from app.models import Package
from app.api.models.package import api, packageDetails, packageInsert
from app.models import db
from app.helpers import token_required


@api.route('packages')
class PackagesApi(Resource):
    @api.marshal_list_with(packageDetails, envelope='packages')
    def get(self):
        viewPackages = Package.query.all()
        return viewPackages

    @token_required
    @api.expect(packageInsert)
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

    @token_required
    @api.expect(packageInsert)
    def put(self):
        data = api.payload
        if data:
            updatePackage = Package(destination=data['destination'],
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
            db.session.update(updatePackage)
            db.session.commit()
            return {'result': 'Package has been updated'}, 200
        return {'error': {'statusCode': 400,
                          'errorCode': 'E2000',
                          'message': 'Please fill up the form'}}, 400

    @token_required
    @api.expect(packageInsert)
    def delete(self):
        return {'result': 'Package has been deleted'}

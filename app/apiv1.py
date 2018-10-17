from flask import Blueprint
from flask_restplus import Api
from app.api.restful.user import api as user_api
from app.api.restful.package import api as package_api
from app.helpers import authentication
from flask_cors import CORS


apiRoutes = Blueprint('api', __name__, url_prefix='/api/v1')
CORS(apiRoutes)
api = Api(apiRoutes, title='First Choice Travel Hub API',
          version='v1', doc='/documentation', authorizations=authentication)


api.add_namespace(user_api)
api.add_namespace(package_api)

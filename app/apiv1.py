from flask import Blueprint
from flask_restplus import Api
from app.api.restful.user import api as user_api, authentication
from flask_cors import CORS


apiRoutes = Blueprint('api', __name__, url_prefix='/api')
CORS(apiRoutes)
api = Api(apiRoutes, title='First Choice Travel Hub API',
          version='v1', doc='/documentation', authorizations=authentication)


api.add_namespace(user_api)

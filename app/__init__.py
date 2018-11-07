from flask import Flask, redirect, url_for
from os import getenv
from app.models import db
# from app.apiModels import ma
from app.apiv1 import apiRoutes
from app.api.restful.user import bcrypt
from flask_migrate import Migrate
from flask_cors import CORS


# Flask Activation
app = Flask(__name__)

# Set Configurations
secretKey = getenv('SECRET_KEY')
dbUri = getenv('DATABASE_URI')
sqlTrackModifcation = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
corsHeaders = ['content-type', 'X-CLIENT-TOKEN']
# app_dir = path.dirname(__file__)
# root_dir = path.dirname(app_dir)
# dist_dir = path.join(root_dir, 'dist')

# Activate Configurations
app.config['SECRET_KEY'] = secretKey
app.config['SQLALCHEMY_DATABASE_URI'] = dbUri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sqlTrackModifcation


# Activate Extensions
db.init_app(app)
# ma.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)
cors = CORS(app, headers=corsHeaders)


# Activate Blueprints
app.register_blueprint(apiRoutes)


@app.route('/')
def index():
    return redirect(url_for('documentationV1'))


@app.route('/api/v1/documentation')
def documentationV1():
    pass


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()

from flask import Flask, render_template, request
from os import getenv
from app.models import db
# from app.apiModels import ma
from app.apiv1 import apiRoutes
from app.api.restful.user import bcrypt
from flask_migrate import Migrate

# Flask Activation
app = Flask(__name__, static_folder="../dist",
            template_folder="../dist")

# Set Configurations
secretKey = getenv('SECRET_KEY')
dbUri = getenv('DATABASE_URI')
sqlTrackModifcation = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
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

# Activate Blueprints
app.register_blueprint(apiRoutes)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return request.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()

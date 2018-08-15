from flask import Flask
from routes import user
from extensions import db
from exception import InvalidUsage

def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(InvalidUsage)(errorhandler)


def register_blueprints(app):
    app.register_blueprint(user.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    db.init_model()
    register_errorhandlers(app)
    register_blueprints(app)

    return app

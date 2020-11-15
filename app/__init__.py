from flask import Flask
from flask_pymongo import PyMongo

# Globals
DB = PyMongo()

def generate_app():
    """Init Core App"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Init Database
    DB.init_app(app)

    with app.app_context():
        # Import routes
        from . import routes

        # register blueprints
        

        return app
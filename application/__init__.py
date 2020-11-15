from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def generate_app():
    """Init Core App"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    with app.app_context():
        # Import routes
        from application import routes

        return app
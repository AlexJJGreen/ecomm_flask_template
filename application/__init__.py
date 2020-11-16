from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def generate_app():
    """Init Core App"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    #initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():  
        # Import routes
        from application import routes, models
        #create db
        db.create_all()
        return app
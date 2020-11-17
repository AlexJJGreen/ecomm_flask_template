from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

db = SQLAlchemy()
migrate = Migrate()
photos = UploadSet("photos", IMAGES)

def generate_app():
    """Init Core App"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    #initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    configure_uploads(app, photos)
    patch_request_class(app)

    with app.app_context():  
        # Import routes
        from application import routes, models
        #create db
        db.create_all()
        return app
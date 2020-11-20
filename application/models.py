from . import db
from flask_login import UserMixin
from . import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    tags = db.Column(db.String(128), index=True)
    description = db.Column(db.String(512), index=True)
    colour = db.Column(db.String(128), index=True)
    primary_image_loc = db.Column(db.String(128), index=True)
    secondary_image_loc = db.Column(db.String(128), index=True)
    tertiary_image_loc = db.Column(db.String(128), index=True)
    ean = db.Column(db.Integer)
    price = db.Column(db.Integer)
    currency = db.Column(db.String(8), index=True)
    inventory = db.Column(db.Integer)
    units_sold = db.Column(db.Integer)


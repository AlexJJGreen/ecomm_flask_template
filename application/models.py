from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

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

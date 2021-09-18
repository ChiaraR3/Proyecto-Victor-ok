from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    #is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)
    def __repr__(self):
        return '<User %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    city = db.relationship('City', backref='country', lazy=True)
    def __repr__(self):
        return '<Countries %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    users = db.relationship('User', backref='city', lazy=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'),
        nullable=False)
    def __repr__(self):
        return '<Cities %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
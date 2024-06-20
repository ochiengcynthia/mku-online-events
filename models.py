from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    clientname = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'eventname': self.eventname,
            'description': self.description,
            'date': self.date.isoformat(),
            'venue': self.venue,
            'clientname': self.clientname,
        }

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staffname = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'staffname': self.staffname,
            'image': self.image,
        }

class ServiceProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(80), nullable=False)
    products = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'service_type': self.service_type,
            'products': self.products,
        }

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sponsorname = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'sponsorname': self.sponsorname,
            'amount': self.amount,
        }

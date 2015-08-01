from app import db

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    t_url = db.Column(db.String(120), index = True)
    headline = db.Column(db.String(300), index=True)
    t_location = db.Column(db.String(120), db.ForeignKey('locations.id'))

    def __repr__(self):
        return '<Tweets %r>' % (self.t_url)

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(120), index=True, unique=True)
    latitude = db.Column(db.Integer, unique=False)
    longitude = db.Column(db.Integer, unique=False)
    tweets = db.relationship('Tweets', backref='place', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.location)

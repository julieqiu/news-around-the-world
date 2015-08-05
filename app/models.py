from app import db

tweets_locations = db.Table('tags',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('tweet_id', db.Integer, db.ForeignKey('tweets.id')),
    db.Column('location_id', db.Integer, db.ForeignKey('locations.id')),
    db.UniqueConstraint('tweet_id', 'location_id', name='tags_tweet_id_location_id')
)

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    t_url = db.Column(db.String(120), index = True, unique=True)
    headline = db.Column(db.String(300), index=True)
                    
    def __repr__(self):
        return '<Tweets %r>' % (self.t_url)

    def add_location(self, location):
        self.place.append(location)
        return self

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(120), index=True, unique=True)
    latitude = db.Column(db.Integer, unique=False)
    longitude = db.Column(db.Integer, unique=False)
    tags = db.relationship('Tweets', 
                    secondary=tweets_locations, 
                    backref=db.backref('place', 
                            cascade="all", lazy='dynamic'))
    
    def __repr__(self):
        return '<Locations %r>' % (self.location)

    def get_tweets(self):
        return self.tags

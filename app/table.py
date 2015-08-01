from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
db = create_engine('sqlite:///tweets.db')
Base.metadata.create_all(db)

class Tweets(Base):
    __tablename__ = 'tweets' 
    t_url = Column(String(120), primary_key=True)
    headline = Column(String(300), index=True)
    t_location = Column(String(120), ForeignKey('locations.location'))

    def __repr__(self):
        return '<User %r>' % (self.headline)

class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key = True)
    location = Column(String(120), index=True, unique=True)
    tweets = relationship('Tweets', backref='article', lazy='dynamic')

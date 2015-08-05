from app import models, db, news


test = 'http://t.co/xRgNttnWFV'


x = models.Tweets.query.filter_by(t_url=test).first()






tweets = models.Tweets.query.all()
print tweets

for tweet in tweets:
    print tweet.t_url
    print tweet.headline
    print tweet.place.all()

y = models.Locations.query.filter_by(location='Istanbul').first()
print y
locations = models.Locations.query.all()

location = locations[0]
#print location.tags

#for location in locations:
#    print location

#x = 'Singapore'

#ret = db.session.query(exists().where(location.location==x)).scalar()

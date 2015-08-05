from app import app
import app.news
from app import models, db


#tweets = models.Tweets.query.all()
#locations = models.Locations.query.all()

#for tweet in tweets:
#    print tweet


#app.news.remove_tweets_from_database()
#app.news.add_cities_to_database()
app.news.add_tweets_to_database()


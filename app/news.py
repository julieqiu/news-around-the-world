from app import models, db
import twitter
import requests
from bs4 import BeautifulSoup
import json
from cities import *
import re

consumer_key='WcHIHtMgSRypCXsSpy0jkisdm'
consumer_secret='kPZEqFoQaLA4adGEOd5hOigZLtI0aD47piQMZ5O4dF9epKovtz'
access_token_key='57390009-speZZzkpQLO4hqMBxVp6z9AkWziAcgab9lpro2SXa'
access_token_secret='v6S4Ye9rifsSGo30n0IUCzUPp98aLHaXg2qDPeKqW6Lmm'
base_url = 'https://api.twitter.com/1.1/'

news_handles = ['ABC','BBCBreaking', 'BBCWorld']

def get_news(news_handles):
        api = twitter.Api(consumer_key,consumer_secret,
                access_token_key, access_token_secret)

        for handle in news_handles:
            statuses = api.GetUserTimeline(screen_name=handle)
            for status in statuses:
                try:
                    t_url = status.urls[0].url
                    headline = status.text 
                    article = models.Tweets(t_url=t_url, headline=headline, t_location='x') 
                    db.session.add(article)
                except:
                    pass
            db.session.commit()

def get_locations():
    tweets = models.Tweets.query.with_entities(models.Tweets.t_url)
    for item in tweets:
        scrape_url(item.t_url)


test_url = 'http://www.huffingtonpost.com/entry/ap-us-history-framework_55ba1f15e4b0af35367a538d'

test_url2 = 'http://www.nytimes.com/2015/07/31/us/a-psychologist-as-warden-jail-and-mental-illness-intersect-in-chicago.html?hp&action=click&pgtype=Homepage&module=photo-spot-region&region=top-news&WT.nav=top-news'


def scrape_url(url):
    page = requests.get(url)
    html_doc = page.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    article = [p.text for p in soup.findAll('p')] 
    cities = models.Locations.query.all()
    for place in cities:
        city = place.location
        for section in article:
                if re.search(r'\b'+re.escape(city)+r'\b',section):
                    p = models.Locations.query.filter_by(location=city).first()
                    tweet = models.Tweets.query.filter_by(t_url=url).first()
                    tweet.place = p
                    break
    db.session.commit()


def add_cities():
    for city in cities:
        print cities[city] 
        locations = models.Locations(location=cities[city].get('city'),
                                    latitude=cities[city].get('lat'),
                                    longitude=cities[city].get('lon'))
        db.session.add(locations)
    db.session.commit()

    loca = models.Locations.query.all()
    print loca

#c = models.Locations.query.filter_by(location='Chicago').first()
#print c.id
#print c.location
#print c.tweets

#new_cities = requests.get(cities)
#print new_cities.content
#print json.loads(new_cities.content)

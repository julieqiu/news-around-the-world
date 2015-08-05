from app import models, db
import twitter
import requests
from bs4 import BeautifulSoup
import json
from cities import *
import re
import geojson
import json

consumer_key='WcHIHtMgSRypCXsSpy0jkisdm'
consumer_secret='kPZEqFoQaLA4adGEOd5hOigZLtI0aD47piQMZ5O4dF9epKovtz'
access_token_key='57390009-speZZzkpQLO4hqMBxVp6z9AkWziAcgab9lpro2SXa'
access_token_secret='v6S4Ye9rifsSGo30n0IUCzUPp98aLHaXg2qDPeKqW6Lmm'
base_url = 'https://api.twitter.com/1.1/'

news_handles = ['googlenews']

def get_news_from_twitter(new_handles):
        api = twitter.Api(consumer_key,consumer_secret,
                access_token_key, access_token_secret)
        for handle in news_handles:
            statuses = api.GetUserTimeline(screen_name=handle, count=50)
            for status in statuses:
                try:
                    t_url = status.urls[0].url
                    headline = status.text
                    article = models.Tweets(t_url=t_url, headline=headline)
                    db.session.add(article)
                    db.session.commit() 
                except Exception as e:
                    print e
                    db.session.rollback()
                    continue


def get_locations_from_urls():
    tweets = models.Tweets.query.all()
    for tweet in tweets:
        scrape_url(tweet)


def scrape_url(tweet):
    url = tweet.t_url
    page = requests.get(url)
    html_doc = page.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        tweet.headline = soup.title.string
    except:
        print soup.title
        pass
    article = [p.text for p in soup.findAll('p')]
    cities = models.Locations.query.all()
    for place in cities:
        city = place.location
        for section in article:
                if re.search(r'\b'+re.escape(city)+r'\b',section):
                    if not (place in tweet.place.all()): 
                        tweet.place.append(place)
                        print tweet.place
                        db.session.add(tweet)
                        break
    db.session.commit()


def add_tweets_to_database():
    get_news_from_twitter(news_handles)
    get_locations_from_urls()


def add_cities_to_database():
    for city in cities:
        print cities[city]
        locations = models.Locations(location=cities[city].get('city'),
                                    latitude=cities[city].get('lat'),
                                    longitude=cities[city].get('lon'))
        db.session.add(locations)
    db.session.commit()

    loca = models.Locations.query.all()

def remove_tweets_from_database():
    tweets = models.Tweets.query.all()
    for tweet in tweets:
        db.session.delete(tweet)
    db.session.commit()

def create_geojson():
    cities = models.Locations.query.all()
    lst = []
    for location in cities:
        tweets = location.get_tweets()
        if tweets:
            point = geojson.Point((location.longitude, location.latitude))
            properties = {}
            properties['location']=location.location
            articles={}
            for tweet in tweets:
                articles[tweet.headline]=tweet.t_url
            properties['articles']=articles
            feature = geojson.Feature(geometry=point, properties=properties)
            dumps = geojson.dumps(feature)
            lst.append(dumps)
    return lst


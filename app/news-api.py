import requests
from requests_oauthlib import OAuth1Session
import json

consumer_key='WcHIHtMgSRypCXsSpy0jkisdm'
consumer_secret='kPZEqFoQaLA4adGEOd5hOigZLtI0aD47piQMZ5O4dF9epKovtz'
access_token_key='57390009-speZZzkpQLO4hqMBxVp6z9AkWziAcgab9lpro2SXa'
access_token_secret='v6S4Ye9rifsSGo30n0IUCzUPp98aLHaXg2qDPeKqW6Lmm'
twitter = OAuth1Session(consumer_key, consumer_secret, 
                    access_token_key, access_token_secret)
base_url = 'https://api.twitter.com/1.1/'
    
def get_data(subdomain, params={'format': 'json'}):
    url = base_url + subdomain 
    response = twitter.get(url, params=params)
    return response.json()

def post_data(subdomain, params={'format': 'json'}): 
    url = base_url + subdomain 
    response = twitter.post(url, params=params)
    return response.json()

result = get_data('statuses/user_timeline.json', {'format':'json', 'screen_name':'abc'})

print json.loads(result)

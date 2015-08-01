import requests
from urlparse import urlparse


import json
import urllib


client_key='dj0yJmk9UzhPZlRNbmFwQjdZJmQ9WVdrOWNXSlBRM2hOTm1VbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lNw--'
client_secret='8eb66129a2d550779614eb358f3f6bfecac854ef'

params = {'client_id':client_key, 'client_'redirect_url':'https://api.login.yahoo.com/oauth/v2/get_token','response_type':'code'}
string2 = urllib.urlencode(params)

request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
base_authorization_url = 'https://api.login.yahoo.com/oauth2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth2/get_token'
base_url = 'http://yboss.yahooapis.com/geo/placespotter'

string = '?oauth_nonce=ce2130523f788f313f76314ed3965ea6i&oauth_timestamp=1202956957&oauth_consumer_key='+client_key+'&oauth_signature_method=plaintext&oauth_signature='+client_secret+ '&oauth_version=1.0&xoauth_lang_pref=en-us&oauth_callback=oob'  


print base_authorization_url+'?'+string2
response = requests.get(access_token_url+'?'+string2)
print response



def callYahoo(params={'format':'json','outputType':'json'}):
    r = oauth.get(base_url, auth=oauth,params=params)
    return r

params = {
    'documentType':'text/plain',
    'documentContent':'I live in New York City',
    'outputType':'json'
}


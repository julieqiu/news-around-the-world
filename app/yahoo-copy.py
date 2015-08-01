import requests
from requests_oauthlib import OAuth1Session
import json

client_key='dj0yJmk9UzhPZlRNbmFwQjdZJmQ9WVdrOWNXSlBRM2hOTm1VbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lNw--'
client_secret='8eb66129a2d550779614eb358f3f6bfecac854ef'

request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
base_authorization_url = 'https://api.login.yahoo.com/oauth2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth2/get_token'
base_url = 'http://yboss.yahooapis.com/geo/placespotter'

oauth = OAuth1Session(client_key, oauth_consumer_key=client_key)
print oauth.authorization_url(request_token_url)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

authorization_url = oauth.authorization_url(base_authorization_url)
print 'Please go here and authorize,', authorization_url
redirect_response = raw_input('Paste the full redirect URL here: ')
oauth_response = oauth.parse_authorization_response(redirect_response)
verifier = oauth_response.get('oauth_verifier')

auth = OAuth1Session(client_key,
                    client_secret=client_secret,
                    resource_owner_key=resource_owner_key,
                    resource_owner_secret=resource_owner_secret,
                    verifier=verifier)

oauth_tokens = oauth.fetch_access_token(access_token_url)
resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')
oauth = OAuth1Session(client_key,
                    client_secret=client_secret,
                    resource_owner_key=resource_owner_key,
                    resource_owner_secret=resource_owner_secret)



def callYahoo(params={'format':'json','outputType':'json'}):
    r = requests.get(base_url, auth=oauth,params=params)
    return r

params = {
    'documentType':'text/plain',
    'documentContent':'I live in New York City',
    'outputType':'json'
}

print callYahoo(params).text

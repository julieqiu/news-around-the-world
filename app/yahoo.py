import requests
from urlparse import urlparse
import oauth2 as oauth
import time
import json
import urllib


OAUTH_CONSUMER_KEY='dj0yJmk9UzhPZlRNbmFwQjdZJmQ9WVdrOWNXSlBRM2hOTm1VbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lNw--'
OAUTH_CONSUMER_SECRET='8eb66129a2d550779614eb358f3f6bfecac854ef'


def oauth_request(url, params, method="GET"):
    # Removed trailing commas here - they make a difference.
    params['oauth_version'] = "1.0" #,
    params['oauth_nonce'] = oauth.generate_nonce() #,
    params['oauth_timestamp'] = int(time.time())

    consumer = oauth.Consumer(key=OAUTH_CONSUMER_KEY,
                              secret=OAUTH_CONSUMER_SECRET)
    params['oauth_consumer_key'] = consumer.key
    req = oauth.Request(method=method, url=url, parameters=params)
    req.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, None)

    return req


if __name__ == "__main__":
    url = "http://yboss.yahooapis.com/ysearch/web"

    req = oauth_request(url, params={"q": "cats dogs"})
    # This one is a bit nasty. Apparently the BOSS API does not like
    # "+" in its URLs so you have to replace "%20" manually.
    # Not sure if the API should be expected to accept either.
    # Not sure why to_url does not just return %20 instead...
    # Also, oauth2.Request seems to store parameters as unicode and forget
    # to encode to utf8 prior to percentage encoding them in its to_url
    # method. However, it's handled correctly for generating signatures.
    # to_url fails when query parameters contain non-ASCII characters. To
    # work around, manually utf8 encode the request parameters.
    req['q'] = req['q'].encode('utf8')
    req_url = req.to_url().replace('+', '%20')
    result = urllib2.urlopen(req_url)
    print result

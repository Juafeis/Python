import oauth2 as oauth
import urllib2 as urllib
import json

# See Assignment 1 instructions or README for how to get these credentials
consumer_key = "qDqiLQoTgQusOGa9x0YJJtXr8"
consumer_secret = "HBb2eOxW1XbO1ERIul0UR0zN3MDNz4P1IF6UKqA1qjdXcSBVL4"
 
access_token_key  = "2792071239-0ewaqKRyFglUAPDjDEjEEikn292OE1rjjFVR9cN"
access_token_secret  = 'xnQimJigJSReMjoCF0WmMpO2nz0dSmjKbTxyUpkg23LJL'

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  return json.load(response)
#  for line in response:
#    print line.strip()

#if __name__ == '__main__':
#   fetchsamples()

myResults = fetchsamples()
print (myResults)


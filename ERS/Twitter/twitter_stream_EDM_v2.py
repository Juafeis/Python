
# coding: utf-8

# In[9]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream




consumer_key = "qDqiLQoTgQusOGa9x0YJJtXr8"
consumer_secret = "HBb2eOxW1XbO1ERIul0UR0zN3MDNz4P1IF6UKqA1qjdXcSBVL4"
 
access_token  = "2792071239-0ewaqKRyFglUAPDjDEjEEikn292OE1rjjFVR9cN"
access_token_secret  = 'xnQimJigJSReMjoCF0WmMpO2nz0dSmjKbTxyUpkg23LJL'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter tweets with geoposition .
    stream.filter(locations=[-180,-90,180,90])


# In[ ]:




import tweepy
import json
# import keys
from racist_terms import black

# get keys
consumer_key = "YcSWh2b8K7GYGOjRePhbFicPg"
consumer_secret = "HaMix0UmqHggYDcbF4uEiA9J4UluiiKGNTdr2PgicGzEYQI3Ns"
access_token = "503080507-PHn1HQtclSxSBvindsRHZNWV0BAr8Br6ELuRAW2x"
access_token_secret = "mp1vP93iw7lEVmKwqbwHvsbM05VfqRCAoZRFI9BQXJe7T"

#autheticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

response = api.get_user('ronessaacquesta')
print(json.dumps(response, indent = 4, sort_keys=False))
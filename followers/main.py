# Dependencies
import tweepy
import json

# Twitter API Keys
consumer_key = "YcSWh2b8K7GYGOjRePhbFicPg"
consumer_secret = "HaMix0UmqHggYDcbF4uEiA9J4UluiiKGNTdr2PgicGzEYQI3Ns"
access_token = "503080507-PHn1HQtclSxSBvindsRHZNWV0BAr8Br6ELuRAW2x"
access_token_secret = "mp1vP93iw7lEVmKwqbwHvsbM05VfqRCAoZRFI9BQXJe7T"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)



# ------------------

# List of users we want to see if our matched people also follow
popFollowing = ['reuters', 'nytimes','washingtonpost', 'buzzfeednews',
			'cnn','realdonaldtrump', 'berniesanders','hillaryclinton',
			'foxnews', 'breitbartnews','seanhannity', 'mike_pence' ]

# test name
screen_name = "CNN"

# Get all user id's following a specified user
followers_id = api.friends_ids(screen_name)

# Loop through all tweets and get the ID's of users
for tweet in followers_id['ids'][0:5]:
	##Utilize JSON dumps to generate a pretty-printed json of 
	# print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))

	# get the twitter screen name from the id input
	screen_name_from_id = api.get_user(tweet)

	# Prints the screen name from the ID loop
	print(screen_name_from_id["screen_name"])



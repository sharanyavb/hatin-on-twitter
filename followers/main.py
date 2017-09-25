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

# # List of users we want to see if our matched people also follow
popFollowing = ['reuters', 'nytimes','washingtonpost', 'buzzfeednews',
			'cnn','realdonaldtrump', 'berniesanders','hillaryclinton',
			'foxnews', 'breitbartnews','seanhannity', 'mike_pence' ]

# test list:
screen_name = ["mewriah", "strangerloops"]

# put followers into a list
followers = []

# loop through screen names given. ie: screen_name
for name in screen_name:
	# target given name in the screen names list
	followers_id = api.friends_ids(name)

	# Loop through all tweets from a given list and get the ID's of users
	for tweet in followers_id['ids']:

		##Utilize JSON dumps to generate a pretty-printed json of 
		# print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))

		# convert the twitter id to a screen name by inputing ID into .get_user api
		screen_name_from_id = api.get_user(tweet)

		if(screen_name_from_id["followers_count"] > 10000):
			# Prints the screen name from the ID loop 
			print(screen_name_from_id["screen_name"])
			print(screen_name_from_id["followers_count"])

			#append to list of followers
			followers.append(screen_name_from_id["screen_name"])

	print(len(followers))


# can do a breakdown to see if these followers match specified accounts
# if they have x number of followers

import tweepy
import json
# import keys
from racist_terms import black

# get keys
consumer_key = "dhdP8LaOYfkxmxi9Fwde6XtNs"
consumer_secret = "52yu7buJCQdZ44f9niYauSg6aXHLqHUKjZVXM8HqPxYooKPWVB"
access_token = "1570660926-Ck2MtiaK9ys8AiyDUBsgL3RV3in8GigvkcUPRAp"
access_token_secret = "765YZYKpMvfK8PDXWUxCa2yxZKnf5auAiASwpLNxYCbGO"

#autheticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

#data lists
word = []
time = []
text = []
num_hashtags = []
hashtag_list = []
num_user_mentions = []
user_id = []
name = []
screen_name = []
account_creation_time = []
user_tweet_count = []
location = []
num_followers = []
num_following = []
num_retweets = []
num_favorites = []
in_reply_to = []


def search_request(search_term):
    for x in range(6):
        if x == 0:
            end_id = None
        try: #-filter:retweets   #and (not tweet["retweeted"]) and ("RT" not in tweet["text"]) REMOVE RETWEET DUPLICATES
            response = api.search(search_term, lang = "en", count = 100, max_id = end_id, geocode="39.82,-98.57,1500mi")['statuses']
            for tweet in response:
                tweet_text = tweet['text']
                if (search_term in tweet_text and "RT" not in tweet_text): #
                    word.append(search_term)
                    time.append(tweet['created_at'])
                    text.append(tweet['text'])
                    num_hashtags_tweet = len(tweet['entities']['hashtags'])
                    num_hashtags.append(num_hashtags_tweet)
                    hashtags = []
                    if num_hashtags_tweet > 0:
                        for hastag_text in tweet['entities']['hashtags']:
                            hashtags.append(hastag_text['text'])
                    hashtag_list.append(hashtags)
                    num_user_mentions.append(tweet['entities']['user_mentions'])
                    user_id.append(tweet['user']['id'])
                    screen_name.append(tweet['user']['screen_name'])
                    name.append(tweet['user']['name'])
                    account_creation_time.append(tweet['user']['created_at'])
                    user_tweet_count.append(tweet['user']['statuses_count'])
                    location.append(tweet['user']['location']) 
                    num_followers.append(tweet['user']['followers_count'])
                    num_following.append(tweet['user']['friends_count'])
                    num_retweets.append(tweet['retweet_count'])
                    num_favorites.append(tweet["favorite_count"])  
                    in_reply_to.append(tweet["in_reply_to_user_id"])  

            # print(location)
            # print(coordinates)
            end_id = response[-1]['id'] - 1
        except: 
            print('Error on word: %s' % (search_term))

# for term in black:
#     slur = term.lower()
#     search_request(slur)
#     print("Results for %s: %s" % (term, len(word)))

search_request('trump')
print(location)
print(text)


# user_location = []
# profile_location = []
# timezone = []


# def user_location():
#     for name in screen_name:
#         try: #-filter:retweets   #and (not tweet["retweeted"]) and ("RT" not in tweet["text"])
#             response = api.get_user(name)
#             for tweet in response:
#                 user_location.append(response["location"])
#                 profile_location.append(response["profile_location"])
#                 timezone.append(response["time_zone"])
#         except: 
#             print('Error on word: %s' % (name))


# user_location()

# print(user_location)
# print(profile_location)
# print(timezone)



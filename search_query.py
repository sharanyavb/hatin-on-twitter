import tweepy
import json

from hate_speech1 import race_dict
<<<<<<< HEAD
import pandas as pd
=======
# import keys

>>>>>>> fcba6551bea6c926cbacdc988d18d8a41a6ef3f1

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
race_list = []
phrase = []
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


phrase_list = []

def search_phrase(race):
    for name in race_dict[race]:
        race = name
        phrase0 = race + ' people are'
        phrase1 = race + ' are'
        phrase2 = 'all ' + race + ' are'
        phrase3 = 'i hate ' + race
        phrase4 = 'i hate all ' + race
        phrase5 = 'down with the ' + race
        phrase_list.append(phrase0)
        phrase_list.append(phrase1)
        phrase_list.append(phrase2)
        phrase_list.append(phrase3)
        phrase_list.append(phrase4)
        phrase_list.append(phrase5)

# def search_phrases(phrase_list):
#         for entry in phrase_list: 
#             print(entry)

def search_request(race_name, search_term):
    page_num = 1
    for x in range(10):
        if x == 0:
            end_id = None
        try: #-filter:retweets   #and (not tweet["retweeted"]) and ("RT" not in tweet["text"]) REMOVE RETWEET DUPLICATES
            response = api.search(search_term, lang = "en", count = 100, max_id = end_id) #geocode="39.82,-98.57,1500mi")['statuses']
            for tweet in response:
                tweet_text = tweet['text']
                if ("RT" not in tweet_text): 
                    print('Success 1')
                    race_list.append(race_name)
                    phrase.append(search_term)
                    time.append(tweet['created_at'])
                    text.append(tweet['text'])
                    num_hashtags_tweet = len(tweet['entities']['hashtags'])
                    num_hashtags.append(num_hashtags_tweet)
                    hashtags = []
                    if num_hashtags_tweet > 0:
                        for hastag_text in tweet['entities']['hashtags']:
                            hashtags.append(hastag_text['text'])
                    hashtag_list.append(hashtags)
                    num_user_mentions.append(len(tweet['entities']['user_mentions']))
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
                    print('Success 2!')
            end_id = response[-1]['id'] - 1
            print("Search Results Found for %s: page # %s" % (search_term, page_num))
        except: 
            print('Error on phrase: %s, page # %s' % (search_term, page_num))
            break
        page_num += 1

# for term in black:
#     slur = term.lower()
#     search_request(slur)
#     print("Results for %s: %s" % (term, len(word)))

<<<<<<< HEAD
# for key in race_dict.keys():
#     print(key)
#     search_phrase(key)
#     print(phrase_list)
#     for phrase in phrase_list:
#         search_request(key, phrase)
#         phrase_list = []
=======

for key in race_dict.keys():
    search_phrase(key)
    for phrase in phrase_list:
        search_request(key, phrase)
>>>>>>> fcba6551bea6c926cbacdc988d18d8a41a6ef3f1

search_request('black', 'i hate black')
print(location)
print(race_list)
for n in text:
    print(n)
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

racist_df = pd.DataFrame({
    #"race": race_list,
    "phrase": phrase,
    "time": time,
    "tweet": text,
    "# of hastags": num_hashtags,
    "# of mentions": num_user_mentions,
    "screen name": screen_name,
    "user id": user_id,
    "name": name,
    "account creation date": account_creation_time,
    "number of account tweets": user_tweet_count,
    "location": location,
    "# followers": num_followers,
    "# following": num_following,
    "# retweets of tweet": num_retweets,
    "# favorite of tweet": num_favorites,
    "in reply to": in_reply_to
})

racist_df.head()

# print(user_location)
# print(profile_location)
# print(timezone)



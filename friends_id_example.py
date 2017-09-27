import tweepy
import json
#import keys
#from hate_speech1 import race_dict
import pandas as pd

# get keys
consumer_key = "dhdP8LaOYfkxmxi9Fwde6XtNs"
consumer_secret = "52yu7buJCQdZ44f9niYauSg6aXHLqHUKjZVXM8HqPxYooKPWVB"
access_token = "1570660926-Ck2MtiaK9ys8AiyDUBsgL3RV3in8GigvkcUPRAp"
access_token_secret = "765YZYKpMvfK8PDXWUxCa2yxZKnf5auAiASwpLNxYCbGO"

#autheticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

def find_friends(user_id):
    more_friends  = True
    cursor_num = -1
    while(more_friends):  
        response = api.friends_ids(id = user_id, cursor = cursor_num)
        ###needs code for gathering friend info###
        # response[0]['ids']
        response_pretty = json.dumps(response, indent = 4, sort_keys=False)
        print(response_pretty)
        print(response[0]['next_cursor'])
        cursor_num = response[0]['next_cursor']
        if cursor_num == 0:
            more_friends = False
            
find_friends(1916181008)
# response_pretty = json.dumps(response, indent = 4, sort_keys=False)
# print(response_pretty)
# print(len(response[0]['ids']))
# print(response[0]['next_cursor'])

# coding: utf-8

# # Dependencies

# In[ ]:

import tweepy
import json
import pandas as pd
import matplotlib.pyplot as mpl


# # Twitter API Keys & Auth

# In[ ]:

# Twitter API Keys
consumer_key = "YcSWh2b8K7GYGOjRePhbFicPg"
consumer_secret = "HaMix0UmqHggYDcbF4uEiA9J4UluiiKGNTdr2PgicGzEYQI3Ns"
access_token = "503080507-PHn1HQtclSxSBvindsRHZNWV0BAr8Br6ELuRAW2x"
access_token_secret = "mp1vP93iw7lEVmKwqbwHvsbM05VfqRCAoZRFI9BQXJe7T"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


# ## Test Information

# In[ ]:

twitter_act = '../filtered_results.csv'
screen_name = pd.read_csv(twitter_act)

# screen_name = ["mewriah"] #also works if you add multiple twitter names to check
followers = []
follower_count = []

# screen_name["screen name"].head()


# # Process:
# ## * Loop through list given, get their users, find out how many followers those users have, and find mutual following within list given
# 
# 

# In[ ]:

# loop through screen names given. ie: screen_name
for name in screen_name["screen name"][0:10]:
    try:
        # targets given name in the screen names list
        followers_id = api.friends_ids(name)

        # Loop through all following list of user selected and get the ID's of those users
        for tweet in followers_id['ids']:

            # convert the twitter id to a screen name by inputing ID into .get_user api
            screen_name_from_id = api.get_user(tweet)

            # if this account has more than X followers, add to list and put a counter
            if(screen_name_from_id["followers_count"] >= 500000):
                # Prints the screen name from the ID loop 
                print(screen_name_from_id["screen_name"])
                print(screen_name_from_id["followers_count"])

                if screen_name_from_id["screen_name"] not in followers_id:
                    #append to list of followers
                    followers.append(screen_name_from_id["screen_name"])
                    follower_count.append(screen_name_from_id["followers_count"])
    except:  
        print('error on: ' + str(name))
    #get length of list
    print(len(followers))


# # Data Frame: Top Followers from test list

# In[ ]:

topFollowers = pd.DataFrame(
        {   "User": followers,
            "Follower Count": follower_count,
            
        }
    )
topFollowers[["User","Follower Count"]]
new_topFollowers = topFollowers.set_index(['User'])

del new_topFollowers.index.name

# new_topFollowers["Mutual Followers"] = 0
new_topFollowers.sort_values(['Follower Count'], ascending=False).head(25)



# # Mutual Follower Frequency

# In[ ]:

# get number of occurances of each user
popular_follow = new_topFollowers.index.value_counts().to_frame().reset_index()
popular_follow.head(15)


# # Frequency Within News Source List

# In[ ]:

#News Sources
newsTwitter = ['reuters', 'nytimes','washingtonpost', 'buzzfeednews',
        'cnn','realdonaldtrump', 'berniesanders','hillaryclinton',
        'foxnews', 'breitbartnews','seanhannity', 'mike_pence', 'richardbspencer',
          'GlennBeck', 'rnc', 'tomilahren', 'espn', 'npr']

# put results of news matching
newsMatch = []

for x in new_topFollowers.index:
    # if one of the names matches something in our list of news sources:
    if x.lower() in newsTwitter:
        # print(x)
        newsMatch.append(x)

# create data frame based on results
newsDf = pd.DataFrame(
        {   "User": newsMatch,             
        }
    )    

# get value caounts of each that matched #might throw error, check later
newsDf = newsDf["User"].value_counts()
newsDf.to_frame

newsDf.to_csv('Pop_Following.csv', index=False)


# 

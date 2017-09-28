
# coding: utf-8

# # Dependencies

# In[1]:

import tweepy
import json
import pandas as pd
import matplotlib.pyplot as mpl


# # Twitter API Keys & Auth

# In[2]:

# Twitter API Keys
consumer_key = "muPvHQR0HarenMCQML5ED02Ek"
consumer_secret = "HKNWnr3PfaBSFNBNpxOFzyYwbHJQWn14BkhRFgayD7Ou6s4z8U"
access_token = "503080507-8SbMICG3qnLwnvfafyl00Osus2Zue2LXufSD72S3"
access_token_secret = "fivyES8M2pdta486hA2D3l1kT6klUMlnOmZvBTz5kOgku"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


# ## Test Information

# In[3]:

twitter_act = '../filtered_results.csv'
screen_name = pd.read_csv(twitter_act)

# screen_name = ["mewriah"] #also works if you add multiple twitter names to check
followers = []
follower_count = []

individual_screen_name = screen_name["screen name"].value_counts().to_frame().index
individual_screen_name


# # Process:
# ## * Loop through list given, get their users, find out how many followers those users have, and find mutual following within list given
# 
# 

# In[4]:

# loop through screen names given. ie: screen_name
for name in individual_screen_name[1100:1601]:
    try:
        # targets given name in the screen names list
        followers_id = api.friends_ids(name)

        # Loop through all following list of user selected and get the ID's of those users
        for tweet in followers_id['ids']:
            followers.append(tweet)
            print(tweet)

    except:  
        print('error on: ' + str(name))
    #get length of list
    print(len(followers))



# # Data Frame: Top Followers from test list

# In[5]:

topFollowers = pd.DataFrame(
        {   "User": followers,
#             "Follower Count": follower_count,
            
        }
    )
topFollowers[["User"]] #,"Follower Count"
new_topFollowers = topFollowers.set_index(['User'])

del new_topFollowers.index.name

# new_topFollowers["Mutual Followers"] = 0
new_topFollowers.index.value_counts()

#most popular from following lists


# # Mutual Follower Frequency

# In[6]:

# get number of occurances of each user
popular_follow = new_topFollowers.index.value_counts().to_frame().reset_index()
popular_follow.head(15)

popular_follow.to_csv('follower_frequency1600.csv', index=False)


# In[ ]:




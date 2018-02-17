# -*- coding: utf-8 -*-

# Carlo Carandang, Sentiment Analysis, February 17, 2018

import twitter # Load the Twitter Library
api = twitter.Api(consumer_key='your_key', consumer_secret='your_secret', access_token_key='your_key', access_token_secret='your_secret') #Use your own access tokens
print "-----------------"
print(api.VerifyCredentials()) # Make sure you can authenticate ---------------
print "-----------------"
import unirest # Load the sentiment detection library
# Create the payload
response = unirest.post("https://community-sentiment.p.mashape.com/text/", headers={"X-Mashape-Key": "your_key", "Content-Type":"application/x-www-form-urlencoded", "Accept": "application/json"}, params={"txt": "Today is a good day"}) # Pass in a sample text to analyse
print response.body
print "-----------------"
print "Try and get a users timeline to make sure it works"
statuses = api.GetUserTimeline(screen_name='CarandangCarlo')
print statuses 
print "-----------------"

# Write a script detecting sentiments from a user's tweets (use @CarandangCarlo)
import twitter
import unirest
count = 0.0
api = twitter.Api(consumer_key='your_key', consumer_secret='your_secret', access_token_key='your_key', access_token_secret='your_secret')
statuses = api.GetUserTimeline(screen_name='CarandangCarlo', count=200) #Twitter API call to get @CarandangCarlo's last 200 tweets
total = len(statuses) #Total retrieved (in case there is less than 200 tweets)
pos = 0.0
neg = 0.0
neutral = 0.0
for s in statuses: #Loop over the tweets
    response = unirest.post("https://community-sentiment.p.mashape.com/text/", headers={
            "X-Mashape-Key": "your_key", "Content-Type":"application/x-www-form-urlencoded", "Accept": "application/json"}, params={"txt": s.text}) # Create the payload to query the sentiment detection API, pass in the tweet
#extract the sentiment from the API response payload
    print s.text, response.body['result']['sentiment']
    sentiment = response.body['result']['sentiment']
#Count total pos, neg, add a neutral is you wish
    if sentiment == "Positive":
        pos += 1
    elif sentiment == "Negative":
        neg += 1
    elif sentiment == "Neutral":
        neutral += 1
total = len(statuses)
# calculate percent of positivity and negativity
neg_percent = (neg/total)*100
pos_percent = (pos/total)*100
neutral_percent = (neutral/total)*100
print "-----------------"
print "@CarandangCarlo had the following sentiments for Tweets: "
print "-----------------"
print "Negative: ", neg_percent, "% and Positive: ", pos_percent, "% and Neutral: ", neutral_percent, "%"
print "-----------------"
print "Number of Tweets Analyzed: ", len(statuses)
print "-----------------"

#Write a script that can tell you if a recent event or hashtag is getting a good response or not - your choice of hashtags
hashes = api.GetSearch(raw_query="l=en&q=%23superbowl%20since%3A2018-02-01%20until%3A2018-02-15&src=typd&count=50")
total2 = len(hashes) #Total retrieved
pos2 = 0.0
neg2 = 0.0
neutral2 = 0.0
for h in hashes: #Loop over the tweets
    response2 = unirest.post("https://community-sentiment.p.mashape.com/text/", headers={
            "X-Mashape-Key": "your_key", "Content-Type":"application/x-www-form-urlencoded", "Accept": "application/json"}, params={"txt": h.text}) # Create the payload to query the sentiment detection API, pass in the tweet
#extract the sentiment from the API response payload
    print h.text, response2.body['result']['sentiment']
    sentiment2 = response2.body['result']['sentiment']
#Count total pos, neg, add a neutral is you wish
    if sentiment2 == "Positive":
        pos2 += 1
    elif sentiment2 == "Negative":
        neg2 += 1
    elif sentiment2 == "Neutral":
        neutral2 += 1
# calculate percent of positivity and negativity
neg_percent2 = (neg2/total2)*100
pos_percent2 = (pos2/total2)*100
neutral_percent2 = (neutral2/total2)*100
print "-----------------"
print "The recent event 'superbowl' had the following sentiments for Tweets: "
print "-----------------"
print "Negative: ", neg_percent2, "% and Positive: ", pos_percent2, "% and Neutral: ", neutral_percent2, "%"
print "-----------------"
print "Number of Tweets Analyzed: ", len(hashes)
print "-----------------"

#Write a script that can tell you if the users mentioning or talking to a brand is positive or not and report;
mentions = api.GetSearch(raw_query="l=en&q=Saint%20Mary%27s%20University%20since%3A2018-02-01%20until%3A2018-02-15&src=typd&count=50")
total1 = len(mentions) #Total retrieved
pos1 = 0.0
neg1 = 0.0
neutral1 = 0.0
for m in mentions: #Loop over the tweets
    response1 = unirest.post("https://community-sentiment.p.mashape.com/text/", headers={
            "X-Mashape-Key": "your_key", "Content-Type":"application/x-www-form-urlencoded", "Accept": "application/json"}, params={"txt": m.text}) # Create the payload to query the sentiment detection API, pass in the tweet
#extract the sentiment from the API response payload
    print m.text, response1.body['result']['sentiment']
    sentiment1 = response1.body['result']['sentiment']
#Count total pos, neg, add a neutral is you wish
    if sentiment1 == "Positive":
        pos1 += 1
    elif sentiment1 == "Negative":
        neg1 += 1
    elif sentiment1 == "Neutral":
        neutral1 += 1
total1 = len(mentions)
# calculate percent of positivity and negativity
neg_percent1 = (neg1/total1)*100
pos_percent1 = (pos1/total1)*100
neutral_percent1 = (neutral1/total1)*100
print "-----------------"
print "The brand 'Saint Mary's University' had the following sentiments for Tweets: "
print "-----------------"
print "Negative: ", neg_percent1, "% and Positive: ", pos_percent1, "% and Neutral: ", neutral_percent1, "%"
print "-----------------"
print "Number of Tweets Analyzed: ", len(mentions)
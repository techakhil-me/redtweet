import os
import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import pandas as pd
import numpy as np 



# confidential
consumer_secret = os.environ['consumer_secret']
consumer_key = os.environ['consumer_key']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']
bearer_token = os.environ['bearer_token']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# woied INDIA
woeid = 2282863

analyzer = SentimentIntensityAnalyzer()




# utility functions
def cleanText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #Line removess @ mentions (r tells that the expression is a raw string)
    text = re.sub(r'#', '', text) #Remove #
    text = re.sub(r'RT[\s]+', '', text) #Remove Retweet
    text = re.sub(r'https?:\/\/\S+', '', text) #Remove links
    return text

def updateTweets():
    result = []
    trends = api.get_place_trends(woeid)
    for trend in trends[0]['trends'][:5]:
        public_tweets = api.search_tweets(trend['name'],result_type="recent",tweet_mode = "extended")
        for tweet in public_tweets:
            
            if tweet.full_text.startswith("RT @"):
                # print(tweet.retweeted_status.full_text)
                tweet = tweet.retweeted_status
                # print(f"https://twitter.com/twitter/statuses/{tweet.id}")
                # continue
            # tweet url https://twitter.com/twitter/statuses/{id}
            text = GoogleTranslator(source='auto', target='en').translate(tweet.full_text)
            # analysis = TextBlob(text)
            sentiment_dict = analyzer.polarity_scores(text)
            data = {
            "username":tweet.user.screen_name,
                # "location":
            "polarity":sentiment_dict["compound"]*100,
            "topic":trend['name'],
            "text": tweet.full_text,  
            "date":tweet.created_at ,
            "url":f"https://twitter.com/twitter/statuses/{tweet.id}",
            "action":False,
            "id":tweet.id,
            "retweet":tweet.retweet_count,
            "score":sentiment_dict["compound"]*100,
            "type":"negative"
            }
            result.append(data)
    return result
            

def getTweet(id):
    tweet = api.lookup_statuses(id=[id,])[0]
    text = GoogleTranslator(source='auto', target='en').translate(tweet.text)
    sentiment_dict = analyzer.polarity_scores(text)
    # print(sentiment_dict)
    sentiment_dict["url"] = f"https://twitter.com/twitter/statuses/{tweet.id}"
    sentiment_dict["pos"] = round(sentiment_dict["pos"]*100,2)
    sentiment_dict["neg"] = round(sentiment_dict["neg"]*100,2)
    sentiment_dict["neu"] = round(sentiment_dict["neu"]*100,2)
    return sentiment_dict


def getUser(id):
    user = api.get_user(id)
    posts = api.user_timeline(screen_name = id, count = 200, language = "en", tweet_mode = "extended")
    df = pd.DataFrame([GoogleTranslator(source='auto', target='en').translate(tweet.full_text) for tweet in posts], columns = ["Tweets"])
    
    
    data = {
        "name": user.name,
        "description":user.description,
        "location": user.location,
        "created_at": user.created_at,
        "followers": user.followers_count,
        "followings": user.friends_count,
        "is_bot": False,
        # " "
    }
import os
import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

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

def updateTweets():
    result = []
    trends = api.get_place_trends(woeid)
    for trend in trends[0]['trends'][:5]:
        public_tweets = api.search_tweets(trend['name'],result_type="recent",count=5,tweet_mode = "extended")
        for tweet in public_tweets:
            if tweet.retweeted:
                continue
            # tweet url https://twitter.com/twitter/statuses/{id}
            text = GoogleTranslator(source='auto', target='en').translate(tweet.full_text)
            # analysis = TextBlob(text)
            sentiment_dict = analyzer.polarity_scores(text)
            data = {
            "polarity":sentiment_dict["compound"]*100,
            "topic":trend['name'],
            "text": tweet.full_text,  
            "date":tweet.created_at ,
            "url":f"https://twitter.com/twitter/statuses/{tweet.id}",
            "action":False,
            "id":tweet.id,
            "retweet":tweet.retweet_count,
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
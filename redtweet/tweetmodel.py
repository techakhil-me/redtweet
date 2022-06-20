import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

# confidential
consumer_secret = "w3gDNOGJN7NNfvdN8UhBCEoC7sT3yAAQxBgSBKWvMrpgsB4Y4s"
consumer_key = "urwyOZqtO59hNkSF4RYcqw910"
access_token = "1324255654471561216-ZRQEhUCEa1Z8CMNUUWA3ElvODViuyN"
access_token_secret = "cEvn44hfzb7knQAdf0D3w4ZOG3Wc8WLYbERzkgCZ7ks5S"
bearer_token = "AAAAAAAAAAAAAAAAAAAAALtQdwEAAAAAdqsJ2yfd1jHqrX5h5M%2BCjg206xI%3DUdFIwnO342D5logDEqDQuS0bQ93RkKfKBvC1ebNIXnVADlq3Ef"


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
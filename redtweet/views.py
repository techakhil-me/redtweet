from django.shortcuts import render
from . import tweetmodel
from redtweet.models import Tweets
# Create your views here.
def Home(request):
    high = Tweets.objects.filter(polarity="high")
    low = Tweets.objects.filter(polarity="low")
    medium = Tweets.objects.filter(polarity="medium")
    action = Tweets.objects.filter(action=True)
    context={"high":len(high),"medium":len(medium),"low":len(low),"action":action}
    return render(request, 'index.html',context=context)

def Update(request):
    result = tweetmodel.updateTweets()
    for tweet in result:
        if -100<=tweet["polarity"]<-40:
            tweet["polarity"]="high"
        elif -40<=tweet["polarity"]<-20:
            tweet["polarity"]="medium"
        elif -20<=tweet["polarity"]<0:
            tweet["polarity"]="low"
        else: continue
        new = Tweets(**tweet)
        new.save()
    context = {"result":result}
    return render(request,'update.html',context=context)

def High(request):
    tweets = Tweets.objects.filter(polarity="high")
    context = {"tweets":tweets}
    return render(request,'update.html',context=context)
    
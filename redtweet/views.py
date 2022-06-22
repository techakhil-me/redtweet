from django.shortcuts import render
from . import tweetmodel
from redtweet.models import Tweets
# Create your views here.
def Home(request):
    high = Tweets.objects.filter(polarity="high").filter(action=False)
    low = Tweets.objects.filter(polarity="low").filter(action=False)
    medium = Tweets.objects.filter(polarity="medium").filter(action=False)
    action = Tweets.objects.filter(action=True)
    context={"high":len(high),"medium":len(medium),"low":len(low),"tweets":action}
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
    if request.method == "POST":
        id = request.POST['id']
        tweet = Tweets.objects.get(id=id)
        tweet.action = True
        tweet.save()
        print(id)
    tweets = Tweets.objects.filter(polarity="high").filter(action=False)
    context = {"tweets":tweets}
    return render(request,'tweets.html',context=context)

def Medium(request):
    if request.method == "POST":
        id = request.POST['id']
        tweet = Tweets.objects.get(id=id)
        tweet.action = True
        tweet.save()
        print(id)
    tweets = Tweets.objects.filter(polarity="medium").filter(action=False)
    context = {"tweets":tweets}
    return render(request,'tweets.html',context=context)

def Low(request):
    if request.method == "POST":
        id = request.POST['id']
        tweet = Tweets.objects.get(id=id)
        tweet.action = True
        tweet.save()
        print(id)
    tweets = Tweets.objects.filter(polarity="low").filter(action=False)
    context = {"tweets":tweets}
    return render(request,'tweets.html',context=context)
    
def Test(request):
    context = {"url":False}
    if request.method == "POST":
        link = request.POST['link']
        id = link.split('/')[-1]
        context = tweetmodel.getTweet(id)
    return render(request,'test.html',context=context)
    
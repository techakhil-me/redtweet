from django.db import models

# Create your models here.
class Tweets(models.Model):
    username = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    text = models.CharField(max_length=500, default='null')
    date = models.DateTimeField(blank=True, null=True) 
    polarity = models.CharField(max_length=100, default="low",choices=[("high", "high"), ("medium", "medium"),("low", "low")])
    url = models.CharField(max_length=500, default='null')
    action = models.BooleanField()
    id = models.CharField(max_length=100,primary_key=True)
    retweet = models.IntegerField( default=0)
    score = models.IntegerField( default=0)
    type = models.CharField(max_length=200, default='null')
    def __str__(self):
        return self.topic
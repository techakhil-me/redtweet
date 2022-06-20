from django.contrib import admin
from redtweet.models import Tweets
# Register your models here.
class TweetsAdmin(admin.ModelAdmin):
    list_display = ('id','topic', 'polarity', 'date', 'text', 'url','retweet','action')
    list_filter = ('polarity', 'action')


admin.site.register(Tweets, TweetsAdmin)
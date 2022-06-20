from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('update', views.Update, name="Update"),
    path('high', views.High, name="High"),
    path('test', views.Test, name="Test"),
    # path('login', views.Login, name="login"),   
]
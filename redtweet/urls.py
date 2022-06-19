from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('update', views.Update, name="Update"),
    # path('login', views.Login, name="login"),   
]
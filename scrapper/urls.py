
from django.contrib import admin
from django.urls import path , include
from scrapper import views


urlpatterns = [
     path('', views.home_View , name = "homeView" ),
]

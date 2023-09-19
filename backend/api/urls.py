from django.contrib import admin
from django.urls import path
from .views import Hello 
urlpatterns = [

    path('test', Hello.as_view(), name='register'),

]
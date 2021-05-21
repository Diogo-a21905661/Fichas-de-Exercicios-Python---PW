#  hello/urls.py

from sys import path
from django.shortcuts import render
from . import views

app_name = href="{% url 'website:home' %}"

urlpatterns = [
    path('home', views.home_page_view, name='home')
]
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('view', views.view_page_view, name='view'),
]
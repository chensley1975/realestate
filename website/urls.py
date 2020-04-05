from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('houses.html', views.houses, name="houses"),
    path('contact.html', views.contact, name="contact"),
]
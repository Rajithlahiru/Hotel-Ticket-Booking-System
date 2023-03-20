from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name='index'),
    path("gallery", views.gallery, name='gallery'),
    path("facilities", views.facilities, name='facilities'),
]
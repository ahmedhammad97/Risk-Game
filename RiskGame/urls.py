from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('play', views.play)
]
urlpatterns += staticfiles_urlpatterns()

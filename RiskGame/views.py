from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import controller

def index(request):
    return render(request, 'index.html')

def play(request):
    controller.prepareGame(request)
    return render(request, 'play.html')

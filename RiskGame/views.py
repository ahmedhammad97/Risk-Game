from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import controller

def index(request):
    return render(request, 'index.html')

def play(request):
    controller.prepareGame(request) #Create Game class and playing agents

    try:
        if(request.POST['map']=="egypt"):
            return render(request, 'playEgypt.html')
        elif(request.POST['map']=="us"):
            return render(request, 'playUS.html')
    except:
        return render(request, 'error.html')

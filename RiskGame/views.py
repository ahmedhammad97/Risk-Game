from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import controller

def index(request):
    return render(request, 'index.html')

def play(request):
    try:
        map, playerOne, playerTwo, data
        if(request.POST['map']=="egypt"):
            data["map"] = "Egypt"
            return render(request, 'playEgypt.html')
        elif(request.POST['map']=="us"):
            data["map"] = "Usa"
            return render(request, 'playUS.html')

        data["playerOne"] = request.POST['playerOne']
        data["playerTwo"] = request.POST['playerTwo']

        controller(data) #Create Game class and playing agents

    except:
        return render(request, 'error.html')

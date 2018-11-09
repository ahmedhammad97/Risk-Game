from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import controller

def index(request):
    return render(request, 'index.html')

def play(request):
    try:
        data = {}
        data["playerOne"] = request.POST['playerOne']
        data["playerTwo"] = request.POST['playerTwo']

        if(request.POST['map']=="egypt"):
            data["map"] = "Egypt"
        elif(request.POST['map']=="us"):
            data["map"] = "Usa"

        controller.prepare(data) #Create Game class and playing agents

        if(request.POST['map']=="egypt"):
            return render(request, 'playEgypt.html')
        elif(request.POST['map']=="us"):
            return render(request, 'playUS.html')

    except Exception as e:
        print(e)
        return render(request, 'error.html')

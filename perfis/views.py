from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Bem Vindo ao Connectedin!")
    return render(request, 'index.html')
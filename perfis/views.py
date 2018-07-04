from django.http import HttpResponse
from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    #return HttpResponse("Bem Vindo ao Connectedin!")
    return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def exibir(request, perfil_id):
    #print("Entrou e deu certo o id de perfil {}".format(perfil_id))

    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html', {'perfil' : perfil})
from django.http import HttpResponse
from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    #return HttpResponse("Bem Vindo ao Connectedin!")
    return render(request, 'index.html')

def exibir(request, perfil_id):
    #print("Entrou e deu certo o id de perfil {}".format(perfil_id))

    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Mogan', 'moganrz@gmail.com', '123456', 'Mogans LTDA')

    if perfil_id == 2:
        perfil = Perfil('Aline', 'aline@gmail.com', '888888', 'Aline LTDA')

    return render(request, 'perfil.html', {'perfil' : perfil})
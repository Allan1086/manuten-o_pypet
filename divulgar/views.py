from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from divulgar.models import *
from divulgar.forms import *

# Create your views here.

@login_required
def cadastrar_pet(request):
    if request.method == 'GET':
        form = CadastrarPet()
        return render(request, 'cadastrar_pets.html', {'form':form})
    
    elif request.method == 'POST':
        form = CadastrarPet(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            messages.add_message(request, constants.SUCCESS, 'Pet cadastrado com sucesso!')
            return render(request, 'castrar_pets.html')
        else:
            messages.add_message(request, constants.ERROR, 'Não foi possivel cadastrar, verifique os dados')
            return render(request, 'cadastrar_pets.html', {'form':form})


@login_required
def seus_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(usuario=request.user)
        return render(request, 'seus_pets.html', {'pets': pets})
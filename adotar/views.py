from django.shortcuts import render, HttpResponse, redirect
from divulgar.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
@login_required
def listar_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        return render(request, 'listar_pets.html', {'pets': pets})
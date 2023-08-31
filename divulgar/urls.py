from django.urls import path
from divulgar.views import *

urlpatterns = [
    path('', cadastrar_pet, name='cadastrar_pet'),
    path('seus_pets/', seus_pets, name='seus_pets')
    
]
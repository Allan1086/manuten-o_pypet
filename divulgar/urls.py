from django.urls import path
from divulgar.views import *

urlpatterns = [
    path('', cadastrar_pet, name='cadastrar_pet'),
    path('seus_pets/', seus_pets, name='seus_pets'),
    path('detalhar_pet/<int:id>/', detalhar_pet, name='detalhar_pet'),
    path('remover_pet/<int:id>/', remover_pet, name='remover_pet'),
]
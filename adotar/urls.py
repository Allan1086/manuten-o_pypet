from django.urls import path
from adotar.views import *


urlpatterns = [
    path('', listar_pets, name='listar_pets'),
] 

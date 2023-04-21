


from django.contrib import admin
from django.urls import path, include
from .views import *
import Encuentra_GasolineraAPP

urlpatterns = [
    path('',carga_pagina),
    path('login/',logeo),
    path('usuario/',usuario_conectado),
    path('registro/',registro),
    path('logout/',desloguearse)
]
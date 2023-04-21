from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect

from .decorators import *
from .models import *
from django.contrib.auth.hashers import make_password
# Create your views here.
def carga_pagina(request):
    return render(request,'PaginaInicial.html')

def logeo(request):

    form = AuthenticationForm()

    if request.method == "GET":
        return render(request, "Login.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        # Verificar que el formulario es valido
        if form.is_valid():
            # Intentar loguear
            user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password'), )

            # Si hemos encontrado el usuario
            if user is not None:
                # Nos logueamos
                login(request, user)
                return render(request, 'Paginalogeado.html')

        else:
            # pasar errores a la vista
            error = "Credenciales incorrectas"
            return render(request, "Login.html", {"form": form,
                                                  'error': error})
    #return render(request,'Login.html')
@user_required
def desloguearse(request):
    logout(request)
    return render(request,"PaginaInicial.html")
def usuario_conectado(request):
    return render(request,'Paginalogeado.html')

def registro(request):
    if request.method=="GET":
        return render(request,'Registro.html')
    else:
        nuevo_usuario= Usuario()
        nuevo_usuario.email = request.POST.get("correo")
        nuevo_usuario.username = request.POST.get("name")
        nuevo_usuario.password = make_password(request.POST.get("pass"))
        nuevo_usuario.password2 = make_password(request.POST.get("pass2"))
        if request.POST.get("correo") == '' or request.POST.get("name") == '' or request.POST.get("pass") == '':
            error = "Rellena todos los campos"
            return render(request, 'Registro.html', {'error': error})
        elif request.POST.get("pass") != request.POST.get("pass2"):
            error = "Las contraseñas no coinciden"
            return render(request, 'Registro.html', {'error': error})
        elif Usuario.objects.filter(email = request.POST.get("correo")).exists() or Usuario.objects.filter(username = request.POST.get("name")).exists():
            error = "Este usuario ya existe"
            return render(request, 'Registro.html', {'error': error})
        else:
            Usuario.save(nuevo_usuario)
            return redirect('/Encuentra_GasolineraAPP/usuario')

              # falta poner un mensaje


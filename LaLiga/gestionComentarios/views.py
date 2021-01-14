from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required()
def verifica(request):
    return True



def home(request):
    verifica_login = False
    if verifica(request):
        verifica_login = True
    return render(request, "gestionComentarios/home.html",{"verifica":verifica_login})


'''
Donde tengo que ir si la página esta protegida solo para usuarios registrados


@login_required(login_url='/accounts/login/')
def partidos(request):
    return render(request, "gestionComentarios/partidos.html")    

'''

'''

def buscar(request):

    if request.GET["email"]:

        busqueda = request.GET["email"]

        usuario = Usuario.objects.filter(email__icontains = busqueda)

        return render(request, "home-login.html", {"usuario":usuario, "query":busqueda})

    else:
        mensaje = "El campo esta vacio"  


    

    return HttpResponse(mensaje)

'''



from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json


'''
Para hacer peticiones a un servidor podemos usar 
python -m pip install requests => lleva una (s) a diferencia del request
'''


# Create your views here.


'''
Donde tengo que ir si la página esta protegida solo para usuarios registrados
'''

@login_required(login_url='/accounts/login/')
def partidos(request):

    listaClasificaciones = requests.get("http://api.bdfutbol.com?u=aleagustin&ps=bolita22&tip=cla&cat=1a&temp=2020-21&format=json")

    clasificaciones = listaClasificaciones.json()

    return render(request, "gestionPartidos/partidos.html",{'clasificaciones' : clasificaciones})  



'''
IMPORTANTE
Mostrar como ordeno por ID ya que en la respuesta del api viene desordenados los Ids
'''

@login_required(login_url='/accounts/login/')
def resultados(request):
    listaResultados = requests.get("http://api.bdfutbol.com/?u=aleagustin&ps=bolita22&tip=res&cat=1a&temp=2020-21&format=json")

   # resultados = listaResultados.json()
    
    lista = json.loads(listaResultados.text)

   # lista_resultados = lista['resultado']


    resultados = {"resultados" : sorted(lista["resultado"], key=lambda d: d["id_partido"])}



    return render(request, "gestionPartidos/resultados.html",{'resultados' : resultados})  







 




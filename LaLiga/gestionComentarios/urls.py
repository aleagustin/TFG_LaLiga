from django.urls import path
from gestionComentarios import views
from django.contrib.auth.views import LoginView

'''
Importante name="Home" es el nombre por el que en el href de base
puedo linkearlo href="{% url 'Home'%}" con la ruta del navegador
Importante ponerlo tal cual si empieza por mayuscula ponerlo 

El login debe de redireccionar en settings hacer =>

'''
urlpatterns = [
    path('home/', views.home, name="Home"),
 ##   path('partidos/', views.partidos, name="Partidos"),
    
]

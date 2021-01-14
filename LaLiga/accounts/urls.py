from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView

'''
Importante name="Home" es el nombre por el que en el href de base
puedo linkearlo href="{% url 'Home'%}" con la ruta del navegador
Importante ponerlo tal cual si empieza por mayuscula ponerlo 

El login debe de redireccionar en settings hacer =>

'''
urlpatterns = [
   path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
   path('register/', views.registerView, name='register'),
]

 
 
 
 
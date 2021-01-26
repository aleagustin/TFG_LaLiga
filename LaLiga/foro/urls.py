from django.urls import path
from foro import views
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('foroselect/', views.foroselect, name="Foroselect"),
    path('foro/<int:id>', views.foro, name="Foro"),
    
]
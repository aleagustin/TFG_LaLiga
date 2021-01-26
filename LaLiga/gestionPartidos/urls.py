from django.urls import path
from gestionPartidos import views


urlpatterns = [
   # Le puse partidos pero es clasificación pero por no cambiarlo deje partidos
   path('partidos/', views.partidos, name="Partidos"),
   path('resultados/', views.resultados, name="Resultados")
    
]

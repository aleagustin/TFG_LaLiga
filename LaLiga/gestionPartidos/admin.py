from django.contrib import admin
from gestionPartidos.models import Clasificacion, Partidos


## Con esta linea hago que aparezca en Admin para administrar Comentarios


# Register your models here.
admin.site.register(Clasificacion)
admin.site.register(Partidos)


class PartidoAdmin(admin.ModelAdmin):
    list_display = ("nombre_visitante","nombre_local","estadio","fecha")

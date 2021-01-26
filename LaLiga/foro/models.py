from django.db import models

from django.contrib.auth.models import User
from gestionPartidos.models import Partidos
import datetime

# Create your models here.

class Comentario(models.Model):
    
    contenido = models.CharField(max_length=255)
    publicado = models.BooleanField(default=True)
    fecha = models.DateField(default=datetime.date.today)
    id_usuario = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='comentario')
    id_partido = models.ForeignKey(Partidos,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s " %(self.contenido, self.fecha, self.id_usuario)

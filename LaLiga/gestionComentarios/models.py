##from django.db import models
#import datetime
'''
class Usuario(models.Model):
    nombre = models.CharField(max_length=25)
    email = models.EmailField()
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return (self.nombre)


def __str__(self):
    return "%s %s" %(self.name, self.email)
'''
'''    
class Comentario(models.Model):
    contenido = models.CharField(max_length=255)
    publicado = models.BooleanField()
    fecha = models.DateField(default=datetime.date.today)

'''
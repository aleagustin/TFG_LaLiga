from django.db import models


class Clasificacion(models.Model):

    posicion = models.CharField(max_length=255)
    id_equipo = models.CharField(max_length=255)
    nombre_equipo = models.CharField(max_length=255)
    puntos = models.CharField(max_length=255)
    pj = models.CharField(max_length=255)
    pg = models.CharField(max_length=255)
    pe = models.CharField(max_length=255)
    pp = models.CharField(max_length=255)
    gf = models.CharField(max_length=255)
    gc = models.CharField(max_length=255)




class Partidos(models.Model):
    
    id_partido = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    jornada = models.CharField(max_length=255)
    id_local = models.CharField(max_length=255)
    nombre_local = models.CharField(max_length=255)
    id_visitante = models.CharField(max_length=255)
    nombre_visitante = models.CharField(max_length=255)
    goles_local = models.CharField(max_length=255)
    goles_visitante = models.CharField(max_length=255)
    id_arbitro = models.CharField(max_length=255)
    nombre_arbitro = models.CharField(max_length=255)
    estadio = models.CharField(max_length=255)



    def __str__(self):
        return "%s %s %s %s " %(self.nombre_visitante, self.nombre_local, self.estadio,self.fecha)







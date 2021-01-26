from django.contrib import admin

# Register your models here.


from foro.models import Comentario


## Con esta linea hago que aparezca en Admin para administrar Comentarios
admin.site.register(Comentario)


## Con esto pongo en linea horizontal lo explicado abajo pero para que coja
class ComentarioAdmin(admin.ModelAdmin):
        list_display = ("contenido","fecha","id_usuario")
    

'''
Con esto puedo editar cosas propias de la web de Administración
1- list_display sirve para poder poner en linea horizontal los campos 
propios del usuario o comentario
2- search_field espara tener una barra de busqueda que solo busque por nombre y email
    ya que no tiene sentido buscar por contraseña.
    
    Importante => se deben llamar como los atributos de la clase models
    UsuarioAdmin se puede llamar como queramos lo importante es que herede de admin.ModelAdmin

3- El list_filter pone en la parte lateral un filtro por el nombre de los atributos que queremos
   En este caso van a estar publicados los contenidos de los usuarios pero si por ejemplo queremos
   eliminar un comentario podemos sacarlo de publicación. 

   Importante => la coma final (,) debe ir en list_filter ya que es una tupla y es obligatorio
'''

'''
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre","email") 
    search_fields = ("nombre", "email")
'''   

'''
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("contenido","publicado","fecha") 
    list_filter = ("publicado","fecha",)    
'''
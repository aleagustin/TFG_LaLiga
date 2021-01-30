from django.forms import ModelForm, Textarea
from foro.models import Comentario



class ComentarioForm(ModelForm):
      

      class Meta:
            model = Comentario
            fields = ('contenido',)
         
            labels={
            'contenido':'',
              }
                        
            widgets = {
            'contenido': Textarea(attrs={'cols': 80, 'rows': 10, 'style': "float:right; margin-left:20px"}),
            }


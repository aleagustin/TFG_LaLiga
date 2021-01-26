from django import forms
from foro.models import Comentario



class ComentarioForm(forms.ModelForm):
      class Meta:
            model = Comentario
            fields = ('contenido',)



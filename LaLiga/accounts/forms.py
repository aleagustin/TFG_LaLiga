'''
Creo por mi cuenta forms.py 
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Extendemos del original
'''
Aqui lo que hacemos es editar el formulario por defecto 
que trae django para registrarse.
Ya que este solo tiene username pass1 y pass2 
entonces agregamos email.
Importante ver como se llama cada campo en el modelo
User que es propio de django por eso 
from django.contrib.auth.models import User
'''

class UCFWithEmail(UserCreationForm):
   
    class Meta:
        model = User
        fields = ["username", "email" ,"password1", "password2"]


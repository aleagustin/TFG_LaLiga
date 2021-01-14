from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Estas son las líneas que cambian
from .forms import UCFWithEmail
# Create your views here.



'''
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("Home")
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html',{'form':form})        
'''


'''
Borra campos de ayuda el pass debe tener tanta cantidad de 
caracteres... 
Como vemos en el else tengo tambien llamado a la clase editada
con el email.
Es que apenas entro no esta validando nada y si dejo UserCreationForm
Sera el de por defecto de django que no tiene email
'''

def registerView(request):
    
    
    if request.method == "POST":
        form = UCFWithEmail()
        form = UCFWithEmail(data=request.POST)
       
        if form.is_valid():
           form.save()
           return redirect("Home")
    else:
        form = UCFWithEmail()


    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, 'accounts/register.html',{'form':form})        
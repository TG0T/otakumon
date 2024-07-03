from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Manga, ItemCarrito

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class IngresoManga(forms.ModelForm):
    class Meta:
        model = Manga
        fields = '__all__'

class FormularioItemCarrito(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ('cantidad',)
from django.forms import ModelForm
# from django import forms
from .models import *

class CategoriaForm(ModelForm):
     class Meta:
          model = Categoria
          fields = ['nome', 'ordem']
# class CategoriaForm(forms.Form):     
#      nome = forms.CharField(max_length = 100, label = 'Produto:', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o nome do produto'}))
#      ordem = forms.IntegerField(label = 'Ordem:', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Informe a ordem do produto'}))
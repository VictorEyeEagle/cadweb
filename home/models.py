import locale
from django.db import models
# from .forms import *

class Categoria(models.Model): 
    nome = models.CharField(max_length = 100)
    ordem = models.IntegerField()

    def __str__(self):
        return self.nome


# class MeuFormulario(forms.Form):
#     nome_completo = forms.CharField(validators=[validar_nome()])
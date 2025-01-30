from django.forms import ModelForm
from django import forms
from .models import *
from datetime import date

class CategoriaForm(forms.ModelForm):
     class Meta:
          model = Categoria
          fields = ['nome', 'ordem',]
          # exclude = ['senha',]  #Exclui campos especificos 
          widgets = {
               'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'style': 'margin-bottom::15px'}),
               'ordem': forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': 'Ordem'}),
          }
          labels = {
               'nome': 'Informe o nome do produto: ',
               'ordem': 'Informe o número da ordem: ',
          }

     def clean_nome(self):
          nome = self.cleaned_data.get('nome')
          if not self.instance.pk:  # Verifica se exite id, caso não exita verificar o valor colocado se já existe ou não
               if Categoria.objects.filter(nome=nome).exists():
                    raise forms.ValidationError("Já existe uma categoria com esse mesmo nome.")
          if len(nome) < 3:
               raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")          
          return nome
     
     def clean_ordem(self):
          ordem = self.cleaned_data.get('ordem')
          if not self.instance.pk:
               if Categoria.objects.filter(ordem=ordem).exists():
                    raise forms.ValidationError("O númera da ordem digitada já esta sendo utilizada.")
          if ordem <= 0:
               raise forms.ValidationError("O campo ordem tem que ser superior a 0.")
          return ordem
     

class ClienteForm(forms.ModelForm):
     class Meta:
          model = Cliente 
          fields = ['nome', 'cpf', 'datanasc',]
          widgets = {
               'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
               'cpf':forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
               'datanasc':forms.DateInput(attrs={'class': 'data form-control', 'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
          }

     def clean_nome(self):
         nome = self.cleaned_data.get('nome')
        #  if Cliente.objects.filter(nome=nome).exclude(pk=self.instance.pk).exists():
        #      raise forms.ValidationError("Já existe um cliente com esse nome.")
         if len(nome) < 3:
             raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
         return nome

     def clean_cpf(self):
         cpf = self.cleaned_data.get('cpf')
         if Cliente.objects.filter(cpf=cpf).exclude(pk=self.instance.pk).exists():
             raise forms.ValidationError("Já existe uma pessoa com esse C.P.F.")
         if len(cpf) != 14:  # Exemplo: "000.000.000-00"
             raise forms.ValidationError("O C.P.F. deve conter 11 caracteres.")
         return cpf

     def clean_datanasc(self):
         datanasc = self.cleaned_data.get('datanasc')
         if datanasc >= date.today():
             raise forms.ValidationError("A data de nascimento não pode ser maior ou igual a data atual.")
         return datanasc
     

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria','img_base64']
        widgets = {
          #   'categoria': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.HiddenInput(),
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'img_base64': forms.HiddenInput(), 
            'preco':forms.TextInput(attrs={
                'class': 'money form-control',
                'maxlength': 500,
                'placeholder': '0.000,00'
            }),
        }
        
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço do Produto',
        }


    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].localize = True
        self.fields['preco'].widget.is_localized = True 

class EstoqueForm(forms.ModelForm):
     class Meta:
          model = Estoque
          fields = ['produto', 'qtde']

          widgets = {
               'produto': forms.HiddenInput(),
               'qtde': forms.TextInput(attrs={'class': 'inteiro form-control',}),
          }  
   

class PedidoForm(forms.ModelForm):
     class Meta:
          model = Pedido
          fields = ['cliente']
          widgets = {
               'cliente': forms.HiddenInput(),
          }


class ItemPedidoForm(forms.ModelForm):
     class Meta:
          model = ItemPedido
          fields = ['pedido', 'produto', 'qtde']

          widgets = {
               'pedido': forms.HiddenInput(),
               'produto': forms.HiddenInput(),
               'qtde': forms.TextInput(attrs={'class': 'inteiro form-control',}),
          }
     
     # def clean(self):
     #      cleaned_data = super().clean()
     #      nome = cleaned_data().get('nome')
     #      ordem = cleaned.data().get('ordem')

     #      if len(nome) < 3:
     #           raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
     #      return nome

     # Validação generica:
     # def validar_valor(valor):
     #      if len(valor) < 3:
     #           raise forms.ValidationError("O campo deve ter pelo menos 3 caracteres.")
     #      return valor
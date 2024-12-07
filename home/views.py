from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def categoria(request): 
    contexto = {
        'lista': Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/lista.html', contexto)

def form_categoria(request):
    if (request.method == 'POST'):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.nome = form.data['nome']
            categoria.ordem = form.data['ordem']
            categoria.save()
            return redirect('lista')
    else: 
        form = CategoriaForm()
    
    contexto = {
        'form': form,
    }
    return render(request, 'categoria/formulario.html', contexto)


def editar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    if (request.method == 'POST'):
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            lista=[]
            lista.append(categoria)
            return redirect('categoria', {'lista': lista})
            # categoria.nome = form.data['nome']
            # categoria.ordem = form.data['ordem']
            # categoria.save()
    else: 
        form = CategoriaForm(instance=categoria)
    
    # contexto = {
    #     'form': form,
    # }
    return render(request, 'categoria/formulario.html', {'form':form,})
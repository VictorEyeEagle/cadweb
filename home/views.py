from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def categoria(request): 
    contexto = {
        'lista': Categoria.objects.all().order_by('-id'),
    }
    return render(request, 'categoria/lista.html', contexto)

def form_categoria(request):
    if (request.method == 'POST'):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            salvando = form.save()
            lista=[]
            lista.append(salvando)
            messages.success(request, 'Operação concluida!')
            return render(request, 'categoria/lista.html', {'lista':lista,})
        
    else: 
        form = CategoriaForm()
    
    return render(request, 'categoria/formulario.html', {'form': form,})


def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    if (request.method == 'POST'):
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            lista=[]
            lista.append(categoria)
            return render(request, 'categoria/lista.html', {'lista':lista,})

    else: 
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria/formulario.html', {'form':form,})


def remover_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        messages.success(request, 'Exclusão bem sucedida!')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')
    
    return redirect('lista')
    # return render(request, 'categoria/lista.html')


def detalhe_categoria(request, id):
    try:
        categoria = get_object_or_404(Categoria, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    return render(request, 'categoria/detalhes.html', {'categoria':categoria,})
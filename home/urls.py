from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #CATEGORIAS:
    path('categoria/lista', views.categoria, name="lista"),
    path('categoria/formulario', views.form_categoria, name='form_categoria'),
    path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('remover_categoria/<int:id>/', views.remover_categoria, name='remover_categoria'),
    path('detalhe_categoria/<int:id>', views.detalhe_categoria, name='detalhe_categoria'),
    #CLIENTES:
    path('cliente/lista', views.cliente, name='listaCliente'),
    path('cliente/formulario', views.form_cliente, name='form_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>/', views.remover_cliente, name='remover_cliente'),
    path('detalhe_cliente/<int:id>', views.detalhe_cliente, name='detalhe_cliente'),
    #PRODUTOS:
    path('produto/lista', views.produto, name='listaProduto'),
    path('produto/formulario', views.form_produto, name='form_produto'),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>/', views.remover_produto, name='remover_produto'),
    path('detalhe_produto/<int:id>', views.detalhe_produto, name='detalhe_produto'),
    #ESTOQUE:
    path('ajustar_estoque/<int:id>/', views.ajustar_estoque, name='ajustar_estoque')
]
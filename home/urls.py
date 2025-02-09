from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # CATEGORIAS:
    path('categoria/lista', views.categoria, name="lista"),
    path('categoria/formulario', views.form_categoria, name='form_categoria'),
    path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('remover_categoria/<int:id>/', views.remover_categoria, name='remover_categoria'),
    path('detalhe_categoria/<int:id>', views.detalhe_categoria, name='detalhe_categoria'),
    # CLIENTES:
    path('cliente/lista', views.cliente, name='listaCliente'),
    path('cliente/formulario', views.form_cliente, name='form_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>/', views.remover_cliente, name='remover_cliente'),
    path('detalhe_cliente/<int:id>', views.detalhe_cliente, name='detalhe_cliente'),
    # PRODUTOS:
    path('produto/lista', views.produto, name='listaProduto'),
    path('produto/formulario', views.form_produto, name='form_produto'),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>/', views.remover_produto, name='remover_produto'),
    path('detalhe_produto/<int:id>', views.detalhe_produto, name='detalhe_produto'),
    # ESTOQUE:
    path('ajustar_estoque/<int:id>/', views.ajustar_estoque, name='ajustar_estoque'),
    # TESTE:
    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name='buscar_dados'),
    path('teste3/', views.teste3, name='teste3'),
    # PEDIDO:
    path('pedido/lista', views.pedido, name='listaPedido'),
    path('pedido/novo_pedido/<int:id>', views.novo_pedido, name='novo_pedido'),
    path('detalhes_pedido/<int:id>', views.detalhes_pedido, name='detalhes_pedido'),
    path('editar_pedido/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('remover_pedido/<int:id>/', views.remover_pedido, name='remover_pedido'),
    path('remover_item_pedido/<int:id>/', views.remover_item_pedido, name='remover_item_pedido'),
    path('editar_item_pedido/<int:id>/', views.editar_item_pedido, name='editar_item_pedido'),
    path('form_pagamento/<int:id>/', views.form_pagamento, name='form_pagamento'),
    path('remover_pagamento/<int:id>/', views.remover_pagamento, name='remover_pagamento'),
]
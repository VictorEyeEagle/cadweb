from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/lista', views.categoria, name="lista"),
    path('categoria/formulario', views.form_categoria, name='form_categoria'),
    path('detalhe_categoria/<int:id>', views.detalhe_categoria, name='detalhe_categoria'),
    path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('remover_categoria/<int:id>/', views.remover_categoria, name='remover_categoria'),
]
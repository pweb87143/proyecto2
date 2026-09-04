from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_cliente, name='index_cliente'),
    path('clientes/', views.cliente_listar, name='cliente_listar'),
    path('clientes/crear/', views.cliente_crear, name='cliente_crear'),
]
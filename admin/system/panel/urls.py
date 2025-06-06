from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns=[
    
    path('',views.index,name='index'),
    ################################################################################################
    path('listar_productos/', views.listar_productos, name='listar_productos'),

    ################################################################################################

    path('ventas/', views.ventas, name='ventas'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/editar/<int:id>/', views.editar_venta, name='editar_venta'),

    # Rutas para Venta2
    path('ventas2/', views.ventas2, name='ventas2'),
    path('ventas2/agregar/', views.agregar_venta2, name='agregar_venta2'),
    path('ventas2/editar/<int:id>/', views.editar_venta2, name='editar_venta2'),

    ################################################################################################
    ################################################################################################
    path('clientes',views.clientes,name='clientes'),
    path('agregar_clientes/', views.agregar_cliente, name='agregar_cliente'),
    path('editar_cliente/<str:dni>/', views.editar_cliente, name='editar_cliente'),


    ################################################################################################
    ################################################################################################
    ################################################################################################
    path('listar',views.listar,name='listar'),
    path('agregar',views.agregar,name='agregar'),
    path('actualizar',views.actualizar,name='actualizar'),
    path('eliminar',views.eliminar,name='eliminar'),
    ################################################################################################
    ################################################################################################
    ################################################################################################
    ################################################################################################
    path('listarconjuntolicra',views.listar_cdlicra,name='listarconjuntolicra'),
    path('pedidoconjuntolicra',views.pedido_cdlicra,name='pedidoconjuntolicra'),
    ################################################################################################
    ################################################################################################
    ################################################################################################
    ################################################################################################
    path('listarconjuntonova',views.listar_cdnova,name='listarconjuntonova'),
    path('pedidoconjuntonova',views.pedido_cdnova,name='pedidoconjuntonova'),


]
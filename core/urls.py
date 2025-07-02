from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('ingresar/', views.IngresoUsuario.as_view(), name='ingresar'),
    path('registro/', views.registro_usuario, name='registro'),
    path('salir/', views.SalirUsuario.as_view(), name='salir'),
    path('inicio/', views.vista_inicio, name='inicio'),

   
    path('listas/', views.lista_listas, name='lista_listas'),
    path('listas/crear/', views.crear_lista, name='crear_lista'),
    path('listas/editar/<int:pk>/', views.editar_lista, name='editar_lista'),
    path('listas/eliminar/<int:pk>/', views.eliminar_lista, name='eliminar_lista'),

    path('', lambda request: redirect('inicio'), name='root_redirect'),
    path('listas/<int:pk>/agregar-canciones/', views.agregar_canciones, name='agregar_canciones'),
    path('listas/<int:pk>/', views.detalle_lista, name='detalle_lista'),
]

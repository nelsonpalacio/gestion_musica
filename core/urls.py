from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Ruta para la página de ingreso (login) usando una clase basada en vista
    path('ingresar/', views.IngresoUsuario.as_view(), name='ingresar'),

    # Ruta para el registro de nuevos usuarios (vista basada en función)
    path('registro/', views.registro_usuario, name='registro'),

    # Ruta para cerrar sesión (logout), clase basada en vista
    path('salir/', views.SalirUsuario.as_view(), name='salir'),

    # Página principal luego de iniciar sesión, vista protegida con login_required
    path('inicio/', views.vista_inicio, name='inicio'),

    # Listado de todas las playlists del usuario autenticado
    path('listas/', views.lista_listas, name='lista_listas'),

    # Crear una nueva playlist (formulario)
    path('listas/crear/', views.crear_lista, name='crear_lista'),

    # Editar una playlist existente identificada por su pk (clave primaria)
    path('listas/editar/<int:pk>/', views.editar_lista, name='editar_lista'),

    # Eliminar una playlist existente (confirmación previa)
    path('listas/eliminar/<int:pk>/', views.eliminar_lista, name='eliminar_lista'),

    # Redirección automática de la raíz del sitio a la página de inicio (login requerido)
    path('', lambda request: redirect('inicio'), name='root_redirect'),

    # Agregar canciones a una playlist específica (pk identifica la playlist)
    path('listas/<int:pk>/agregar-canciones/', views.agregar_canciones, name='agregar_canciones'),

    # Vista detalle de una playlist, muestra sus canciones y metadatos
    path('listas/<int:pk>/', views.detalle_lista, name='detalle_lista'),
]

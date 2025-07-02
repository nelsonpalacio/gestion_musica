from django.contrib import admin
from django.urls import path, include

"""
Archivo principal de rutas (urls.py) del proyecto gestion_musica.

Define las URL globales que incluyen:
- La ruta para acceder al panel de administración de Django.
- La inclusión de las URLs definidas en la app 'core' para la funcionalidad principal.
"""

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta al panel de administración
    path('', include('core.urls')),  # Incluye las URLs de la app 'core' para la web principal
]

from django.contrib import admin
from .models import ListaReproduccion, Cancion

"""
Registro de modelos en el panel de administración de Django.

Permite gestionar desde el admin las listas de reproducción y las canciones.
"""

# Registrar el modelo ListaReproduccion para gestión desde el admin
admin.site.register(ListaReproduccion)

# Registrar el modelo Cancion para gestión desde el admin
admin.site.register(Cancion)

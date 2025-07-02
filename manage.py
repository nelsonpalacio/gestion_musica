#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Este archivo es el punto de entrada para ejecutar comandos administrativos 
de Django desde la consola, como levantar el servidor, aplicar migraciones, 
crear superusuarios, entre otros.

Ejemplo de uso:
    python manage.py runserver
    python manage.py migrate
"""

import os
import sys

def main():
    """
    Configura el entorno para usar las configuraciones del proyecto y 
    ejecuta el comando recibido desde la línea de comandos.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_musica.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Manejo del error si Django no está instalado o no está en el path
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecuta el comando recibido desde la consola (sys.argv)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

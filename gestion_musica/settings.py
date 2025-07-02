"""
Archivo de configuración principal de Django para el proyecto gestion_musica.

Generado automáticamente con 'django-admin startproject' y adaptado para el proyecto.

Documentación oficial: 
- Configuración general: https://docs.djangoproject.com/en/5.2/topics/settings/
- Referencia completa: https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Construcción de rutas absolutas dentro del proyecto, facilita manejo de archivos.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración rápida para desarrollo. En producción, modificar estos valores para seguridad y rendimiento.

# Clave secreta del proyecto. Mantenerla segura y no subirla a repositorios públicos.
SECRET_KEY = 'django-insecure-7k6bnqb@!hnzis-ab(2mr8$7f76qim1h8a#^zo=z!qwz1vbc8*'

# Activar o desactivar modo debug. Nunca activar en producción.
DEBUG = True

# Hosts permitidos para servir la aplicación.
ALLOWED_HOSTS = ['gestion-musica.onrender.com', 'localhost', '127.0.0.1']


# Aplicaciones instaladas en el proyecto, incluyendo apps propias y de terceros.
INSTALLED_APPS = [
    # Apps predeterminadas de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App principal del proyecto
    'core',

    # Paquete para facilitar la personalización de widgets en formularios
    'widget_tweaks',
]

# Middleware: Capas intermedias que procesan la petición/respuesta HTTP.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Manejo de autenticación
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo que contiene las rutas principales del proyecto
ROOT_URLCONF = 'gestion_musica.urls'

# Configuración de los templates (plantillas HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Directorios extra donde buscar plantillas (vacío porque se usan templates dentro de apps)
        'APP_DIRS': True,  # Busca templates dentro de carpetas 'templates' en cada app
        'OPTIONS': {
            'context_processors': [  # Variables globales para las plantillas
                'django.template.context_processors.request',  # Permite acceso a 'request' en templates
                'django.contrib.auth.context_processors.auth',  # Variables de usuario autenticado
                'django.contrib.messages.context_processors.messages',  # Mensajes flash
            ],
        },
    },
]

# Aplicación WSGI para despliegue
WSGI_APPLICATION = 'gestion_musica.wsgi.application'


# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos SQLite (por defecto para desarrollo)
        'NAME': BASE_DIR / 'db.sqlite3',  # Ruta al archivo de base de datos
    }
}


# Validadores de contraseña para mejorar seguridad
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Configuración de localización e internacionalización
LANGUAGE_CODE = 'en-us'  # Idioma predeterminado
TIME_ZONE = 'UTC'        # Zona horaria

USE_I18N = True  # Activar internacionalización
USE_TZ = True    # Usar zonas horarias


# Configuración para servir archivos estáticos (CSS, JS, imágenes)
STATIC_URL = 'static/'


# Tipo de campo predeterminado para claves primarias en modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuraciones de URLs para redirección luego de login/logout
LOGIN_REDIRECT_URL = '/inicio/'      # Página a mostrar tras login exitoso
LOGOUT_REDIRECT_URL = '/ingresar/'   # Página tras logout
LOGIN_URL = '/ingresar/'              # URL para login (usada por decoradores)

#  Music App - Proyecto de Gestión de Playlists Musicales

Aplicación web desarrollada con **Django** que permite a los usuarios autenticarse, crear, editar y gestionar listas de reproducción personalizadas, así como añadir canciones a sus playlists.
---
##  Estructura del Proyecto
gestion_musica/
│
├── core/ # Aplicación principal
│ ├── models.py # Modelos: Cancion y ListaReproduccion
│ ├── views.py # Vistas para CRUD de listas y autenticación
│ ├── forms.py # Formularios personalizados
│ ├── urls.py # Rutas de la aplicación
│ ├── admin.py # Registro en el panel de administración
│ ├── tests.py # Tests (en blanco por ahora)
│ └── templates/core/ # HTMLs para vistas
│
├── gestion_musica/ # Configuración global del proyecto
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py / asgi.py
│
├── manage.py # Script de gestión
└── requirements.txt # Dependencias del proyecto
---

##  Documentación de Código

### `models.py`

```python
class Cancion(models.Model):
    """
    Modelo que representa una canción.
    Atributos:
        - titulo (str): Título de la canción
        - artista (str): Nombre del artista
    """
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class ListaReproduccion(models.Model):
    """
    Modelo que representa una lista de reproducción musical.
    Atributos:
        - usuario (User): Propietario de la lista
        - nombre (str): Nombre de la lista
        - descripcion (str): Descripción opcional
        - fecha_creacion (datetime): Fecha de creación automática
        - canciones (ManyToMany): Canciones asociadas
    """
    def __str__(self):
        return self.nombre
    ---------------------------------------------------  
##  Forms.py

class FormularioRegistroUsuario(UserCreationForm):
    """
    Formulario personalizado para registrar nuevos usuarios.
    Extiende el formulario base de Django.
    """

class ListaReproduccionForm(forms.ModelForm):
    """
    Formulario para crear/editar una lista de reproducción.
    Campos: nombre, descripción.
    """
class AgregarCancionesForm(forms.ModelForm):
    """
    Formulario para agregar canciones a una lista de reproducción existente.
    Usa checkboxes para seleccionar canciones.
    """
    ----------------------------------------------------
views.py

class IngresoUsuario(LoginView):
    """
    Vista basada en clase para iniciar sesión.
    Usa la plantilla: core/ingreso.html
    """
class SalirUsuario(LogoutView):
    """
    Vista para cerrar sesión de forma segura.
    """
def registro_usuario(request):
    """
    Vista para registrar nuevos usuarios.
    GET: Muestra el formulario
    POST: Guarda nuevo usuario y redirige
    """
@login_required
def lista_listas(request):
    """
    Vista para mostrar todas las listas de reproducción del usuario actual.
    """
@login_required
def crear_lista(request):
    """
    Vista para crear una nueva lista de reproducción.
    """
@login_required
def editar_lista(request, pk):
    """
    Vista para editar una lista de reproducción existente.
    """
@login_required
def eliminar_lista(request, pk):
    """
    Vista para eliminar una lista con confirmación previa.
    """
@login_required
def agregar_canciones(request, pk):
    """
    Vista para agregar canciones existentes a una lista de reproducción.
    """
@login_required
def detalle_lista(request, pk):
    """
    Vista para mostrar detalles de una lista: canciones incluidas, etc.
    """
    ------------------------------------------------------------------
## urls.py (core)

urlpatterns = [
    path('ingresar/', IngresoUsuario.as_view(), name='ingresar'),
    path('registro/', registro_usuario, name='registro'),
    path('salir/', SalirUsuario.as_view(), name='salir'),
    path('inicio/', vista_inicio, name='inicio'),

    path('listas/', lista_listas, name='lista_listas'),
    path('listas/crear/', crear_lista, name='crear_lista'),
    path('listas/editar/<int:pk>/', editar_lista, name='editar_lista'),
    path('listas/eliminar/<int:pk>/', eliminar_lista, name='eliminar_lista'),
    path('listas/<int:pk>/agregar-canciones/', agregar_canciones, name='agregar_canciones'),
    path('listas/<int:pk>/', detalle_lista, name='detalle_lista'),

    path('', lambda request: redirect('inicio'), name='root_redirect'),
]
------------------------------------------------------------------------

## Autenticación

Registro de usuario (/registro/)
Login (/ingresar/)
Logout (/salir/)
Protección con @login_required en todas las vistas privadas
-------------------------------------------------------------------------

## Sitio en Producción
El proyecto está desplegado en:
 https://gestion-musica.onrender.com/

 -------------------------------------------------------------------------
 ## Tecnologías Utilizadas
Categoría	            Tecnología
Backend	                Django 5.2.3
Formularios	            Django Forms
Base de Datos	        SQLite
Frontend	            HTML5, Bootstrap 5, CSS3
Autenticación	        Django Login/Logout
Hosting	                Render.com

----------------------------------------------------------------------------

## Autor

Desarrollado por Jose Nelson Palacio Londoño como parte de una prueba técnica en Django.
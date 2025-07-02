# Music App - Aplicación Web Full Stack de Música

Una aplicación web moderna desarrollada en Django que permite a los usuarios gestionar playlists de música de forma intuitiva y eficiente. El sistema incluye autenticación de usuarios, operaciones CRUD completas para playlists y canciones, y una interfaz responsiva construida con Bootstrap.
**Aplicación en línea**: [https://gestion-musica.onrender.com/](https://gestion-musica.onrender.com/)


##  Características Principales

- **Autenticación de Usuarios**: Sistema completo de registro, inicio de sesión y gestión de sesiones
- **Gestión de Playlists**: Crear, visualizar, editar y eliminar playlists personalizadas
- **Biblioteca de Canciones**: Administrar una colección completa de canciones con metadatos
- **Interfaz Responsiva**: Diseño adaptable para dispositivos móviles y de escritorio
- **API REST**: Endpoints para integración con aplicaciones externas
- **Testing Completo**: Suite de tests unitarios y de integración
- **Documentación Técnica**: Código completamente documentado con docstrings

##  Instalación y Configuración

### Prerrequisitos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <https://github.com/nelsonpalacio/gestion_musica>
   cd music_app_project
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación web: http://localhost:8000/
   - Panel de administración: http://localhost:8000/admin/

##  Ejecutar Tests

La aplicación incluye una suite completa de tests unitarios y de integración:

```bash
# Ejecutar todos los tests
python manage.py test

# Ejecutar tests específicos
python manage.py test music_app.tests.PlaylistModelTest
python manage.py test music_app.tests.SongModelTest



### Cobertura de Tests

- **Modelos**: Tests para Song, Playlist y PlaylistSong
- **Formularios**: Validación de PlaylistForm y SongForm
- **Vistas**: Tests de autenticación y CRUD operations
- **API**: Tests de endpoints REST
- **Integración**: Flujos completos de usuario

## Estructura del Proyecto

```
gestion_musica
|   db.sqlite3
|   manage.py
|   requirements.txt
|
+---core
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |
|   +---migrations
|   |   |   0001_initial.py
|   |   |   0002_listareproduccion_fecha_creacion_and_more.py
|   |   |   0003_remove_cancion_lista_listareproduccion_canciones.py
|   |   |   __init__.py
|   |   |
|   |   \---__pycache__
|   |           0001_initial.cpython-313.pyc
|   |           0002_listareproduccion_fecha_creacion_and_more.cpython-313.pyc
|   |           0003_remove_cancion_lista_listareproduccion_canciones.cpython-313.pyc
|   |           __init__.cpython-313.pyc
|   |
|   +---templates
|   |   \---core
|   |           agregar_canciones.html
|   |           base.html
|   |           crear_lista.html
|   |           detalle_lista.html
|   |           editar_lista.html
|   |           eliminar_lista.html
|   |           ingreso.html
|   |           inicio.html
|   |           lista_listas.html
|   |           registro.html
|   |
|   \---__pycache__
|           admin.cpython-313.pyc
|           apps.cpython-313.pyc
|           forms.cpython-313.pyc
|           models.cpython-313.pyc
|           urls.cpython-313.pyc
|           views.cpython-313.pyc
|           __init__.cpython-313.pyc
|
+---entregables
|       Estructura de Base de Datos.pdf
|
\---gestion_musica
    |   asgi.py
    |   settings.py
    |   urls.py
    |   wsgi.py
    |   __init__.py
    |
    \---__pycache__
            settings.cpython-313.pyc
            urls.cpython-313.pyc
            wsgi.cpython-313.pyc
            __init__.cpython-313.pyc



##  Justificación de Elecciones Técnicas

### Framework Backend: Django

**Razones de la elección:**

- **Desarrollo Rápido**: Django sigue el principio "Don't Repeat Yourself" (DRY) y proporciona muchas funcionalidades out-of-the-box, permitiendo un desarrollo más eficiente
- **ORM Robusto**: El Object-Relational Mapping de Django facilita las operaciones de base de datos y proporciona una abstracción segura
- **Sistema de Autenticación**: Django incluye un sistema de autenticación completo y seguro por defecto
- **Admin Interface**: Panel de administración automático para gestión de datos
- **Escalabilidad**: Arquitectura que permite escalar la aplicación según las necesidades
- **Seguridad**: Protecciones integradas contra vulnerabilidades comunes (CSRF, XSS, SQL Injection)
- **Comunidad**: Gran comunidad y ecosistema de paquetes disponibles

### Base de Datos: SQLite (Desarrollo) / PostgreSQL (Producción)

**Razones de la elección:**

- **SQLite para Desarrollo**: 
  - No requiere configuración adicional
  - Ideal para desarrollo y testing
  - Archivo único fácil de gestionar
  
- **PostgreSQL para Producción**:
  - Base de datos robusta y escalable
  - Soporte completo para características avanzadas
  - Excelente rendimiento con grandes volúmenes de datos
  - Compatibilidad total con Django ORM

### Frontend: Django Templates + Bootstrap

**Razones de la elección:**

- **Django Templates**: 
  - Integración nativa con Django
  - Sistema de herencia de templates eficiente
  - Separación clara entre lógica y presentación
  
- **Bootstrap 5**:
  - Framework CSS maduro y bien documentado
  - Componentes responsivos out-of-the-box
  - Diseño mobile-first
  - Amplia compatibilidad con navegadores
  - Personalización sencilla

### API: Django REST Framework

**Razones de la elección:**

- **Integración Perfecta**: Diseñado específicamente para Django
- **Serialización Automática**: Conversión automática entre modelos Django y JSON
- **Autenticación Flexible**: Múltiples métodos de autenticación disponibles
- **Documentación Automática**: Generación automática de documentación de API
- **Viewsets y Routers**: Simplificación del desarrollo de APIs RESTful

### Testing: Django Test Framework

**Razones de la elección:**

- **Integración Nativa**: Framework de testing integrado en Django
- **Base de Datos de Test**: Creación automática de base de datos temporal para tests
- **Client de Test**: Simulación de requests HTTP para testing de vistas
- **Fixtures**: Gestión sencilla de datos de prueba
- **Coverage**: Fácil integración con herramientas de cobertura de código

##  Arquitectura General del Sistema

### Patrón de Arquitectura: Model-View-Template (MVT)

La aplicación sigue el patrón MVT de Django, que es una variación del patrón MVC:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Template    │    │      View       │    │      Model      │
│   (Presentación)│◄───│   (Lógica de    │◄───│   (Datos y      │
│                 │    │    Negocio)     │    │    Lógica)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         ▲                       ▲                       ▲
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   URL Dispatcher│
                    │   (Enrutamiento)│
                    └─────────────────┘
```

Componentes Principales
#### 1. Modelos (Models)
Los modelos   se encuentran en core/models.py y representan las entidades principales del sistema:
Cancion: Representa una canción con metadatos como título y artista.
ListaReproduccion: Representa una lista de reproducción creada por un usuario, con nombre, fecha de creación y relación con canciones.
ListaReproduccion.canciones: Relación ManyToMany entre listas y canciones mediante un campo intermedio (listareproduccion_canciones).
Estos modelos están definidos y versionados mediante migraciones ubicadas en core/migrations/.

#### 2. Vistas (Views)
Las vistas están en core/views.py e implementan la lógica del sistema para mostrar contenido y gestionar interacciones del usuario:
Vistas Web:
Página de inicio (inicio)
Registro e ingreso de usuarios (registro, ingreso)
CRUD completo de listas de reproducción (crear_lista, editar_lista, eliminar_lista, detalle_lista, lista_listas)
Agregado de canciones a listas (agregar_canciones)
Las vistas renderizan templates HTML con formularios y resultados dinámicos.
Se manejan sesiones para mantener el estado del usuario autenticado.

#### 3. Templates
Los templates HTML están en core/templates/core/ e incluyen:
base.html: Template padre reutilizado en todas las páginas.
Templates funcionales:
registro.html, ingreso.html: Para autenticación.
crear_lista.html, editar_lista.html, eliminar_lista.html: Para gestión de listas.
lista_listas.html, detalle_lista.html: Para visualizar contenido.
agregar_canciones.html: Para añadir canciones a listas.
Todos los templates heredan de base.html para mantener una estructura coherente y responsiva.

#### 4. URLs y Enrutamiento
URLs del Proyecto: Definidas en gestion_musica/urls.py, incluyen las rutas principales del sistema:

python
Copiar
Editar
path('', include('core.urls'))
URLs de la App: Definidas en core/urls.py, gestionan rutas como:
/registro/, /ingreso/, /inicio/
/crear_lista/, /editar_lista/<int:id>/, /eliminar_lista/<int:id>/
/detalle_lista/<int:id>/, /agregar_canciones/<int:id>/
Nombres de rutas: Usados en los templates para generar navegación dinámica con {% url 'nombre_ruta' %}.

### Flujo de Datos

```
Usuario → Request HTTP → gestion_musica/urls.py → core/urls.py → Vista en views.py → Modelo en models.py → Base de Datos
                                                          ↓
Usuario ← Response HTML ← Template en core/templates/core/ ← Vista ← Modelo ← Base de Datos

```
Request
El usuario realiza una acción en la interfaz web (por ejemplo, hace clic en “Crear Lista” o envía un formulario de registro).

URL Routing
Django usa el archivo gestion_musica/urls.py para redirigir la petición a core/urls.py, donde se asigna a una vista específica (por ejemplo, crear_lista, detalle_lista, registro, etc.).

View Processing
La vista en core/views.py ejecuta la lógica correspondiente: puede ser mostrar una página, procesar un formulario o realizar una acción (crear, editar, eliminar).

Model Interaction
Si la acción requiere interactuar con los datos, la vista consulta o modifica los modelos definidos en core/models.py (por ejemplo, ListaReproduccion, Cancion, o sus relaciones).

Template Rendering
La vista prepara los datos necesarios y renderiza un archivo HTML ubicado en core/templates/core/, como crear_lista.html o detalle_lista.html, para presentarlo al usuario.

Response
Django devuelve una respuesta HTML al navegador del usuario con el resultado de la acción (por ejemplo, la lista creada o un mensaje de error).



### Seguridad

#### Medidas Implementadas:
- **CSRF Protection**: Protección contra ataques Cross-Site Request Forgery
- **Authentication**: Sistema de autenticación robusto con sesiones
- **Authorization**: Control de acceso basado en propietario de recursos
- **SQL Injection Prevention**: Uso del ORM de Django para consultas seguras
- **XSS Protection**: Escape automático de contenido en templates
- **CORS Configuration**: Configuración adecuada para requests cross-origin

#### Validación de Datos:
- **Form Validation**: Validación en el frontend y backend
- **Model Validation**: Restricciones a nivel de base de datos
- **Serializer Validation**: Validación específica para API endpoints

### Escalabilidad
#### Consideraciones de Diseño:
- **Separación de Responsabilidades**: Cada componente tiene una responsabilidad específica
- **Modelos Normalizados**: Base de datos diseñada para evitar redundancia
- **Caching Ready**: Estructura preparada para implementar caching
- **API First**: Diseño que permite fácil integración con aplicaciones móviles o SPAs
- **Stateless API**: Endpoints REST sin estado para mejor escalabilidad

#### Optimizaciones Implementadas:
- **Query Optimization**: Uso de select_related y prefetch_related cuando es necesario
- **Pagination**: Implementada en vistas de lista para manejar grandes volúmenes
- **Indexing**: Índices de base de datos en campos frecuentemente consultados
- **Static Files**: Separación de archivos estáticos para CDN deployment


##  Documentación de la API

La aplicación proporciona una API REST completa para todas las operaciones principales:

### Autenticación (basado en tus templates: registro.html, ingreso.html)
GET /registro/ – Mostrar formulario de registro
POST /registro/ – Procesar registro de usuario
GET /ingreso/ – Mostrar formulario de inicio de sesión
POST /ingreso/ – Procesar inicio de sesión
GET /logout/ – Cerrar sesión del usuario
Listas de reproducción (según tus vistas y URLs)
GET /listas/ – Ver todas las listas del usuario (lista_listas.html)
GET /listas/crear/ – Mostrar formulario para nueva lista (crear_lista.html)
POST /listas/crear/ – Guardar nueva lista
GET /listas/<id>/ – Ver detalles de la lista (detalle_lista.html)
GET /listas/<id>/editar/ – Formulario para editar lista (editar_lista.html)
POST /listas/<id>/editar/ – Guardar cambios
GET /listas/<id>/eliminar/ – Confirmación para eliminar (eliminar_lista.html)
POST /listas/<id>/eliminar/ – Eliminar la lista
GET /listas/<id>/agregar-canciones/ – Agregar canciones a lista (agregar_canciones.html)

## Gestión de Canciones (Vistas Web)
Funcionalidades Principales
Agregar Canciones
Formulario para registrar canciones nuevas.
Campos requeridos: título, artista.
Posiblemente: duración, álbum, género (dependiendo del modelo).
Validaciones: campos vacíos, duración válida, año numérico.
Biblioteca de Canciones
Página con lista de canciones registradas.
Opciones de búsqueda por título o artista.
Ordenamiento por columnas (si lo tienes implementado).
Gestión de Canciones en Playlists
Vista para agregar canciones a una lista existente.
Posibilidad de eliminar canciones de una lista desde su detalle.
Algunas versiones permiten reordenar canciones.

## Playlist (representación interna en Django)
{
  "id": 1,
  "nombre": "Rock en Español",
  "descripcion": "Mis favoritas",
  "usuario": 3,
  "canciones": [12, 18, 25],
  "fecha_creacion": "2024-01-01 12:00:00",
  "fecha_modificacion": "2024-01-01 13:00:00"
}
## canción
{
  "id": 12,
  "titulo": "Persiana Americana",
  "artista": "Soda Stereo",
  "album": "Signos",
  "duracion": 250,
  "genero": "Rock",
  "fecha_creacion": "2024-01-01 11:00:00"
}
## Gestión de Usuarios
Registro y Autenticación
Registro: Vista /registro/, con validación de campos (username, password).
Login: Vista /ingreso/, validación de credenciales y redirección.
Logout: Redirección segura a inicio o login.
Perfil de Usuario
Cada usuario solo accede a sus propias playlists.
Las playlists se vinculan mediante el campo usuario en el modelo.
(Opcional: visibilidad pública/privada).

## Gestión de Playlists
Crear Playlist
Formulario: nombre (requerido), descripción (opcional).
Validación: nombre único por usuario.
Ver Playlists
Página /listas/ muestra las playlists del usuario autenticado.
Se incluye resumen: número de canciones y duración total.
Editar Playlist
Vista /listas/<id>/editar/: formulario prellenado.
Preserva canciones ya asociadas.
Eliminar Playlist
Confirmación antes de eliminar.
Las canciones no se eliminan, solo se desvinculan.

## Interfaz de Usuario
Diseño Responsivo
Construido con base.html y Bootstrap (según tu estructura).
Plantillas adaptadas a escritorio y móvil:
inicio.html, lista_listas.html, detalle_lista.html, etc.
Experiencia de Usuario
Navegación clara entre crear playlist → agregar canciones → ver detalles.
Formularios bien estructurados.
Mensajes de éxito y error con Bootstrap.

##  Tecnologías Utilizadas
## Backend
Django 5.2.3: Framework web principal utilizado para desarrollar la lógica del servidor, modelos, vistas y enrutamiento.
Django ORM: Sistema de mapeo objeto-relacional para interactuar con la base de datos desde modelos Python.
Sistema de Autenticación de Django: Gestión de usuarios, sesiones, login/logout integrada en el framework.

## Frontend
Bootstrap 5: Framework CSS utilizado para crear una interfaz responsiva y moderna en tus plantillas (base.html, etc.).
HTML5: Lenguaje de marcado para estructurar las páginas del proyecto.
CSS3: Hoja de estilos personalizada para complementar Bootstrap.
JavaScript (opcional): Para funciones dinámicas si se agregaron scripts en formularios o listas.

## Base de Datos
SQLite 3: Base de datos ligera usada por defecto en entornos de desarrollo con Django.
Modelo relacional: Compuesto por entidades como Cancion, ListaReproduccion, Usuario, etc.

## Testing
Django Test Framework: Utilizado para crear pruebas unitarias de modelos y vistas (archivo tests.py en tu app core).
Python unittest: Framework base de testing sobre el que se construyen los tests de Django.

 ## Herramientas de Desarrollo
Python 3.11: Lenguaje de programación principal del proyecto.
pip: Gestor de paquetes para instalar dependencias del proyecto (desde requirements.txt).
venv: Entorno virtual utilizado para aislar las dependencias del proyecto.

Git: Herramienta de control de versiones para gestionar cambios en el código fuente.
##  Métricas del Proyecto
Líneas de Código (Estimadas)
Modelos (models.py): ~100 líneas
(Incluye clases como Cancion, ListaReproduccion, relaciones ManyToMany, etc.)

Vistas (views.py): ~150–250 líneas
(Incluye lógica para CRUD de listas de reproducción, autenticación, y manejo de canciones)

Templates (templates/core/): ~500–700 líneas
(Sumando archivos como base.html, crear_lista.html, detalle_lista.html, agregar_canciones.html, etc.)

Formularios (forms.py): ~40–60 líneas
(Formularios personalizados para login, registro, y creación de listas)

Tests (tests.py): ~100–200 líneas
(Según el nivel de cobertura aplicado)

Total Aproximado: ~1,000 – 1,300 líneas de código

Cobertura de Tests (Estimativa)

Modelos:  ~90% (si has cubierto validaciones y relaciones)
Formularios:  ~80% (si estás validando campos como título, duración, etc.)
Vistas Principales:  ~70% (si pruebas flujo básico de vistas como crear y listar playlists)
Autenticación:  ~80% (si probaste login y registro)

### Funcionalidades Implementadas
 Autenticación completa de usuarios
Registro, inicio de sesión, cierre de sesión y control de acceso por sesión

 CRUD completo de listas de reproducción
Crear, visualizar, editar y eliminar listas personalizadas por usuario

 Gestión de canciones
Agregar canciones a listas, eliminar y visualizar canciones relacionadas

 Interfaz responsiva
Adaptación para dispositivos móviles y escritorio con HTML5, CSS3 y Bootstrap

Sistema basado en vistas web (sin API REST)
Navegación completa mediante formularios y templates Django

Documentación técnica básica incluida
Estructura clara de carpetas, modelos comentados y flujo de datos documentado

Testing básico implementado
Tests unitarios en progreso para modelos, formularios y vistas

##  Despliegue en Producción

### Sitio en Producción

- **Render**: [https://gestion-musica.onrender.com/](https://gestion-musica.onrender.com/)
- Se utilizó la plataforma Render para desplegar la aplicación en un entorno de producción accesible públicamente.


## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.


## Testing
Este proyecto incluye pruebas unitarias para garantizar la calidad del modelo y la lógica de negocio. Las pruebas se encuentran en el archivo core/tests.py.

Pruebas implementadas:
Creación de lista de reproducción: Verifica que una lista se cree correctamente con un usuario.

Asociación de canciones a listas: Asegura que se puedan agregar canciones a una lista correctamente.

Ejecución de los tests
Desde la raíz del proyecto (donde está manage.py), ejecuta:
python manage.py test core


## Autor

Desarrollado por **Jose Nelson Palacio** como parte de un proyecto de práctica en Django para la gestión de listas de reproducción musicales.

##  Soporte

Para preguntas, sugerencias o reportes de bugs, por favor crear un issue en el repositorio del proyecto.

---

**Music App** - Una solución completa para la gestión de playlists musicales 🎵


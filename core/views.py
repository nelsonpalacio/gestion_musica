from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import FormularioRegistroUsuario, ListaReproduccionForm, AgregarCancionesForm
from .models import ListaReproduccion


class IngresoUsuario(LoginView):
    """
    Vista basada en clase para el login de usuarios.

    Usa el template 'core/ingreso.html' para mostrar el formulario de acceso.
    """
    template_name = 'core/ingreso.html'


class SalirUsuario(LogoutView):
    """
    Vista basada en clase para el logout de usuarios.

    Usa el template 'core/salir.html' para mostrar la confirmación de cierre de sesión.
    """
    template_name = 'core/salir.html'


def registro_usuario(request):
    """
    Vista para registrar un nuevo usuario.

    Si el método es POST, procesa el formulario de registro.
    Si el formulario es válido, crea el usuario, inicia sesión y redirige al inicio.
    Si es GET, muestra el formulario vacío.

    Templates usados:
    - 'core/registro.html' para el formulario de registro.
    """
    if request.method == 'POST':
        formulario = FormularioRegistroUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('inicio')  
    else:
        formulario = FormularioRegistroUsuario()
    return render(request, 'core/registro.html', {'formulario': formulario})


@login_required
def vista_inicio(request):
    """
    Vista protegida que muestra la página de inicio tras login exitoso.

    Templates usados:
    - 'core/inicio.html'
    """
    return render(request, 'core/inicio.html')


@login_required
def lista_listas(request):
    """
    Muestra todas las listas de reproducción del usuario actual ordenadas por fecha de creación descendente.

    Templates usados:
    - 'core/lista_listas.html'

    Contexto:
    - listas: queryset con las listas del usuario
    """
    listas = ListaReproduccion.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'core/lista_listas.html', {'listas': listas})


@login_required
def crear_lista(request):
    """
    Permite al usuario crear una nueva lista de reproducción.

    En POST valida el formulario, asigna el usuario actual y guarda la lista.
    En GET muestra un formulario vacío.

    Templates usados:
    - 'core/crear_lista.html'

    Contexto:
    - form: formulario para crear lista
    """
    if request.method == 'POST':
        form = ListaReproduccionForm(request.POST)
        if form.is_valid():
            nueva_lista = form.save(commit=False)
            nueva_lista.usuario = request.user
            nueva_lista.save()
            return redirect('lista_listas')
    else:
        form = ListaReproduccionForm()
    return render(request, 'core/crear_lista.html', {'form': form})


@login_required
def editar_lista(request, pk):
    """
    Permite al usuario editar una lista de reproducción propia.

    Obtiene la lista por su pk y usuario actual (404 si no existe o no pertenece).
    En POST actualiza la lista con datos validados.
    En GET muestra formulario pre-poblado.

    Templates usados:
    - 'core/editar_lista.html'

    Contexto:
    - form: formulario para editar lista
    - lista: objeto ListaReproduccion a editar
    """
    lista = get_object_or_404(ListaReproduccion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ListaReproduccionForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            return redirect('lista_listas')
    else:
        form = ListaReproduccionForm(instance=lista)
    return render(request, 'core/editar_lista.html', {'form': form, 'lista': lista})


@login_required
def eliminar_lista(request, pk):
    """
    Permite al usuario eliminar una lista de reproducción propia.

    En GET muestra la confirmación.
    En POST elimina la lista y redirige a la lista de listas.

    Templates usados:
    - 'core/eliminar_lista.html'

    Contexto:
    - lista: objeto ListaReproduccion a eliminar
    """
    lista = get_object_or_404(ListaReproduccion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        lista.delete()
        return redirect('lista_listas')
    return render(request, 'core/eliminar_lista.html', {'lista': lista})


@login_required
def agregar_canciones(request, pk):
    """
    Permite agregar canciones existentes a una lista de reproducción.

    Obtiene la lista del usuario actual.
    En POST valida y agrega las canciones seleccionadas.
    En GET muestra el formulario para agregar canciones.

    Templates usados:
    - 'core/agregar_canciones.html'

    Contexto:
    - form: formulario para seleccionar canciones
    - lista: objeto ListaReproduccion destino
    """
    lista = get_object_or_404(ListaReproduccion, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = AgregarCancionesForm(request.POST)
        if form.is_valid():
            canciones = form.cleaned_data['canciones']
            for cancion in canciones:
                lista.canciones.add(cancion)
            return redirect('lista_listas')
    else:
        form = AgregarCancionesForm()

    return render(request, 'core/agregar_canciones.html', {'form': form, 'lista': lista})


@login_required
def detalle_lista(request, pk):
    """
    Muestra el detalle de una lista de reproducción con todas sus canciones.

    Obtiene la lista y sus canciones del usuario actual.

    Templates usados:
    - 'core/detalle_lista.html'

    Contexto:
    - lista: objeto ListaReproduccion
    - canciones: queryset con las canciones asociadas
    """
    lista = get_object_or_404(ListaReproduccion, pk=pk, usuario=request.user)
    canciones = lista.canciones.all() 
    return render(request, 'core/detalle_lista.html', {'lista': lista, 'canciones': canciones})

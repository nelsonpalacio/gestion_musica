from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import FormularioRegistroUsuario, ListaReproduccionForm
from .models import ListaReproduccion
from .forms import FormularioRegistroUsuario, ListaReproduccionForm, AgregarCancionesForm



class IngresoUsuario(LoginView):
    template_name = 'core/ingreso.html'


class SalirUsuario(LogoutView):
    template_name = 'core/salir.html'

def registro_usuario(request):
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
    return render(request, 'core/inicio.html')



@login_required
def lista_listas(request):
    listas = ListaReproduccion.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'core/lista_listas.html', {'listas': listas})

@login_required
def crear_lista(request):
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
    lista = get_object_or_404(ListaReproduccion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        lista.delete()
        return redirect('lista_listas')
    return render(request, 'core/eliminar_lista.html', {'lista': lista})

@login_required
def agregar_canciones(request, pk):
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
    lista = get_object_or_404(ListaReproduccion, pk=pk, usuario=request.user)
    canciones = lista.canciones.all() 
    return render(request, 'core/detalle_lista.html', {'lista': lista, 'canciones': canciones})
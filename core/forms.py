from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ListaReproduccion, Cancion
from .models import Cancion


class FormularioRegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'


class ListaReproduccionForm(forms.ModelForm):
    canciones = forms.ModelMultipleChoiceField(
        queryset=Cancion.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Canciones'
    )

    class Meta:
        model = ListaReproduccion
        fields = ['nombre', 'descripcion', 'canciones']
        labels = {
            'nombre': 'Nombre de la lista',
            'descripcion': 'Descripción',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
from django import forms
from .models import Cancion, ListaReproduccion

class AgregarCancionesForm(forms.ModelForm):
    """
    Formulario para agregar múltiples canciones a una lista de reproducción.

    Campo personalizado:
    - canciones: Permite seleccionar varias canciones mediante checkboxes.

    Se basa en el modelo ListaReproduccion y solo expone el campo 'canciones'.
    """
    canciones = forms.ModelMultipleChoiceField(
        queryset=Cancion.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label='Selecciona las canciones para agregar',
        required=False,  # Permite enviar sin seleccionar canciones
    )

    class Meta:
        model = ListaReproduccion
        fields = ['canciones']

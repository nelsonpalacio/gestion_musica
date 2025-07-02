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


class AgregarCancionesForm(forms.ModelForm):
    canciones = forms.ModelMultipleChoiceField(
        queryset=Cancion.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label='Selecciona las canciones para agregar',
        required=False,
    )

    class Meta:
        model = ListaReproduccion
        fields = ['canciones']
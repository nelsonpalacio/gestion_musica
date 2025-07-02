from django.test import TestCase
from django.contrib.auth.models import User
from .models import ListaReproduccion, Cancion

class ListaReproduccionModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='testuser', password='12345')

    def test_crear_lista_reproduccion(self):
        """Verifica que se cree una lista correctamente"""
        lista = ListaReproduccion.objects.create(
            usuario=self.usuario,
            nombre='Mi Lista',
            descripcion='Descripción de prueba'
        )
        self.assertEqual(str(lista), 'Mi Lista')
        self.assertEqual(lista.usuario.username, 'testuser')

    def test_agregar_cancion_a_lista(self):
        """Verifica que se agregue una canción a una lista"""
        cancion = Cancion.objects.create(titulo='Imagine', artista='John Lennon')
        lista = ListaReproduccion.objects.create(usuario=self.usuario, nombre='Favoritas')
        lista.canciones.add(cancion)

        self.assertIn(cancion, lista.canciones.all())

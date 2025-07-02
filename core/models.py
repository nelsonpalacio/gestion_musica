from django.db import models
from django.contrib.auth.models import User

class Cancion(models.Model):
    """
    Modelo que representa una canción en la biblioteca.

    Atributos:
    ----------
    titulo : CharField
        El título de la canción, con un máximo de 100 caracteres.
    artista : CharField
        El nombre del artista o banda que interpreta la canción, máximo 100 caracteres.

    Métodos:
    --------
    __str__()
        Retorna una representación legible de la canción como "Título - Artista".
    """
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"


class ListaReproduccion(models.Model):
    """
    Modelo que representa una lista de reproducción de un usuario.

    Atributos:
    ----------
    usuario : ForeignKey
        Relación con el modelo User, indicando el dueño de la lista.
    nombre : CharField
        Nombre de la lista de reproducción, máximo 100 caracteres.
    descripcion : TextField
        Descripción opcional de la lista de reproducción.
    fecha_creacion : DateTimeField
        Fecha y hora en la que se creó la lista (automático).
    canciones : ManyToManyField
        Relación muchos a muchos con Cancion, permite asociar múltiples canciones a la lista.

    Métodos:
    --------
    __str__()
        Retorna el nombre de la lista de reproducción.
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listas_reproduccion')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    canciones = models.ManyToManyField(Cancion, blank=True, related_name='listas')

    def __str__(self):
        return self.nombre

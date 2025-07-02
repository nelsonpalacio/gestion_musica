from django.db import models
from django.contrib.auth.models import User

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class ListaReproduccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listas_reproduccion')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    canciones = models.ManyToManyField(Cancion, blank=True, related_name='listas')

    def __str__(self):
        return self.nombre

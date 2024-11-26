from django.db import models


class PalabraFrecuente(models.Model):
    palabra = models.CharField(max_length=100)
    frecuencia = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.palabra

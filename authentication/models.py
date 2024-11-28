from django.db import models

class Suscriptores(models.Model):
    # Define los campos necesarios para el modelo de suscriptores
    email = models.EmailField(unique=True)  # Ejemplo de un campo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Calificacion(models.Model):
    rating = models.IntegerField()

    def __str__(self):
        return f'Calificación: {self.rating}'

class Visitas(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.count)
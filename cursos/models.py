from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)  # Campo para la descripción del curso

    def __str__(self):
        return self.nombre

class Capitulo(models.Model):
    curso = models.ForeignKey(Curso, related_name='capitulos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Video(models.Model):
    capitulo = models.ForeignKey(Capitulo, related_name='videos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255, null=True, blank=True)
    archivo_video = models.FileField(upload_to='videos/')  # Campo para cargar el archivo de video

    def __str__(self):
        return f"Video para {self.capitulo.titulo}"
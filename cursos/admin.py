from django.contrib import admin
from .models import Curso, Capitulo, Video

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1  # Número de formularios vacíos que se mostrarán

class CapituloInline(admin.TabularInline):
    model = Capitulo
    extra = 1  # Número de formularios vacíos que se mostrarán

class CapituloAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

class CursoAdmin(admin.ModelAdmin):
    inlines = [CapituloInline]

admin.site.register(Curso, CursoAdmin)
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(Video)
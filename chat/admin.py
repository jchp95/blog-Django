from django.contrib import admin

# admin.py
from django.contrib import admin
from .models import PalabraFrecuente
from .analisis import analizar_preguntas
from django.urls import path
from django.http import HttpResponseRedirect

class PalabraFrecuenteAdmin(admin.ModelAdmin):
    list_display = ('palabra', 'frecuencia', 'fecha')

    def mostrar_estadisticas(self, request, queryset):
        frecuencias = analizar_preguntas('questions_log.txt')
        
        # Guardar en la base de datos (opcional)
        for palabra, frecuencia in frecuencias:
            PalabraFrecuente.objects.update_or_create(palabra=palabra, defaults={'frecuencia': frecuencia})

        # Crear un contexto para mostrar en el admin
        context = {
            'frecuencias': frecuencias,
        }

        # Renderizar las estadísticas en el admin
        return self.admin_site.admin_view(self.render_estadisticas)(request, **context)

    mostrar_estadisticas.short_description = "Mostrar estadísticas de preguntas"

    def render_estadisticas(self, request, frecuencias):
        from django.shortcuts import render
        return render(request, 'admin/estadisticas.html', {'frecuencias': frecuencias})

    actions = [mostrar_estadisticas]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('estadisticas/', self.admin_site.admin_view(self.mostrar_estadisticas), name='estadisticas'),
        ]
        return custom_urls + urls

admin.site.register(PalabraFrecuente, PalabraFrecuenteAdmin)



from django.urls import path
from .views import  lista_cursos, curso_detail

urlpatterns = [
    path('lista_cursos/', lista_cursos, name='lista_cursos'),
    path('curso/<int:curso_id>/', curso_detail, name='curso_detail'),  # Nueva ruta para el detalle del curso
]
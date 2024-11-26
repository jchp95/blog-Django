from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Capitulo
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import os

######################### CURSOS ############################################
@csrf_protect
@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})

def curso_detail(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    capitulos = curso.capitulos.all()  # Obtener todos los capítulos del curso

    # Para cada capítulo, obtenemos sus videos
    for capitulo in capitulos:
        capitulo.videos_list = capitulo.videos.all()  # Obtener los videos de cada capítulo

    return render(request, 'curso_detail.html', {
        'curso': curso,
        'capitulos': capitulos,
    })
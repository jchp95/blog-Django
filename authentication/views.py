from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import CustomUser_CreationForm  # Asegúrate de que este formulario esté definido
from .models import Suscriptores  # Asegúrate de que este modelo esté definido
import logging
from django.contrib import messages
from .models import Visitas


 #######################   REGISTER  ##########################################
def register(request):
    if request.method == 'POST':
        form = CustomUser_CreationForm(request.POST)
        if form.is_valid() and 'terms' in request.POST:
            user = form.save()
            logger.info(f'Nuevo usuario registrado: {user.username}')  # Registra el nombre de usuario
            
            # Verificar si el correo electrónico ya está en suscriptores
            if not Suscriptores.objects.filter(email=user.email).exists():
                # Incrementar el contador de suscriptores
                new_subscriber = Suscriptores(email=user.email)  # Asumiendo que tienes un campo de email
                new_subscriber.save()
            else:
                messages.warning(request, 'Este correo electrónico ya está registrado como suscriptor.')

            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Por favor, corrige los errores o acepta los términos y condiciones.')
    else:
        form = CustomUser_CreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


################################ LOG IN ######################################################################


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'  # Asegúrate de que esta ruta sea correcta
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('registration/password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html' 

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'  # Asegúrate de que esta ruta sea correcta
    success_url = reverse_lazy('registration/password_reset_complete')  # Redirigir a la vista de completado

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


################################# SUSCRIPTORES Y VISTAS ###########################################

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Visitas, Suscriptores, Calificacion  # Asegúrate de tener estos modelos
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg 
import json


# Obtener la cantidad de visitas
def get_visitas(request):
    visitas = Visitas.objects.first()
    if visitas is None:
        # Si no hay registros, devuelve 0 o inicializa uno
        return JsonResponse(0, safe=False)
    return JsonResponse(visitas.count, safe=False)

# Obtener la cantidad de suscriptores
def get_suscriptores(request):
    total_suscriptores = Suscriptores.objects.count()  # Suponiendo que tienes un modelo para suscriptores
    return JsonResponse(total_suscriptores, safe=False)

# Incrementar visitas
@require_POST
def incrementar_visitas(request):
    visitas, created = Visitas.objects.get_or_create(id=1)  # Asegúrate de que haya un registro
    visitas.count += 1  # Incrementa el contador de visitas
    visitas.save()
    return JsonResponse({'status': 'success'})

# Incrementar suscriptores
@require_POST
def incrementar_suscriptores(request):
    # Lógica para agregar un nuevo suscriptor
    # Aquí deberías tener un modelo de Suscriptores y agregar un nuevo registro
    new_subscriber = Suscriptores()  # Asumiendo que tienes un modelo de Suscriptores
    new_subscriber.save()
    return JsonResponse({'status': 'success'})


@csrf_exempt
def calificar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rating = data.get('rating')

        # Guardar la calificación en la base de datos
        Calificacion.objects.create(rating=rating)

        # Calcular el promedio de calificaciones
        average = Calificacion.objects.aggregate(Avg('rating'))['rating__avg']
        
        return JsonResponse({'average': round(average, 1)})  # Retorna el promedio redondeado a 2 decimales
    
    elif request.method == 'GET':
        # Calcular el promedio de calificaciones
        average = Calificacion.objects.aggregate(Avg('rating'))['rating__avg']
        return JsonResponse({'average': round(average, 1)})  # Retorna el promedio redondeado a 2 decimales

    return JsonResponse({'error': 'Método no permitido'}, status=405)
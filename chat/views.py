import json
import requests
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class ChatResponseView(View):
    def get(self, request):
        return render(request, 'chat.html')  # Renderiza la plantilla del chat

    @method_decorator(csrf_exempt)  # Deshabilitar CSRF para simplificar (no recomendado para producción)
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()

            if not user_message:
                return JsonResponse({'error': 'El mensaje no puede estar vacío.'}, status=400)

            # Guardar la pregunta en un archivo
            self.log_question(user_message)

            response = self.handle_specific_questions(user_message)
            if response:
                return JsonResponse({'response': response})

            # Llamar a la API de Gemini para otras preguntas
            generated_response = self.call_gemini_api(user_message)
            return JsonResponse({'response': generated_response})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido. Por favor, verifica tu mensaje.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Ocurrió un error inesperado. Por favor, intenta de nuevo más tarde.'}, status=500)

    def log_question(self, question):
        """Guarda la pregunta en un archivo de texto con codificación UTF-8."""
        with open('questions_log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"{question}\n")

    def handle_specific_questions(self, message):
        """Maneja preguntas específicas y devuelve respuestas predefinidas."""
        if "el blog" in message.lower():
            return (
                "¡Hola! Somos el Team EL BLOG. En nuestro equipo, la pasión y la creatividad se unen para llevar tus ideas al siguiente nivel. "
                "Nos encanta colaborar, innovar y encontrar soluciones que realmente marquen la diferencia. "
                "¡Creemos en construir relaciones auténticas con nuestros clientes y hacer que cada proyecto sea una experiencia divertida y exitosa!"
            )
        elif "de que trata el blog" in message.lower() or "de que va el sitio el blog" in message.lower():
            return "El blog trata sobre temas de interés general, incluyendo desarrollo web, diseño, y tendencias en tecnología. ¡Esperamos que lo disfrutes!"

        elif "servicios" in message.lower():
            return (
                "¡Hola! Nuestro objetivo es ayudarle y tenemos una gama de servicios diseñados para hacerle la vida más fácil. "
                "Mira lo que podemos hacer por ti: Diseño creativo, Desarrollo web, Creación de contenido, Gestión de redes sociales, Consultoría y estrategia."
            )
        elif "contactar" in message.lower():
            return (
                "¡Hola! Puedes contactarnos a través de nuestro sitio web, correo electrónico o redes sociales. "
                "Estamos aquí para ayudarte en cualquier momento."
            )
        elif "proceso de trabajo" in message.lower():
            return (
                "¡Hola! Nuestro proceso de trabajo se basa en la colaboración y la creatividad. "
                "Primero, nos reunimos contigo para entender tus necesidades y objetivos. Luego, diseñamos y desarrollamos una estrategia personalizada. "
                "Finalmente, trabajamos juntos para llevar a cabo el proyecto y asegurarnos de que sea un éxito."
            )
        elif "tiempo en el mercado" in message.lower():
            return (
                "¡Hola! Llevamos 1 año en el mercado, ayudando a nuestros clientes a alcanzar sus objetivos y superar sus expectativas."
            )
        elif "diferente" in message.lower():
            return (
                "¡Hola! Lo que nos hace diferentes es nuestra pasión por la creatividad y la innovación. "
                "Nos enfocamos en entender las necesidades únicas de cada cliente y en desarrollar soluciones personalizadas."
            )
        elif "adecuado" in message.lower():
            return (
                "¡Hola! Si estás buscando un equipo de expertos que se preocupen por tus necesidades y objetivos, entonces EL BLOG es adecuado para ti. "
                "Estamos aquí para ayudarte a alcanzar tus metas y superar tus expectativas."
            )
        elif "empezar a trabajar" in message.lower():
            return (
                "¡Hola! Los pasos para empezar a trabajar con nosotros son simples. Primero, nos reunimos contigo para entender tus necesidades y objetivos. "
                "Luego, diseñamos y desarrollamos una estrategia personalizada. Finalmente, trabajamos juntos para llevar a cabo el proyecto."
            )
        elif "proyectos anteriores" in message.lower():
            return (
                "¡Hola! Hemos trabajado en una variedad de proyectos, desde diseño web y desarrollo de aplicaciones hasta creación de contenido y gestión de redes sociales. "
                "Estamos orgullosos de nuestro portafolio y nos encantaría hablar contigo sobre cómo podemos ayudarte con tu próximo proyecto."
            )
        elif "más información" in message.lower():
            return (
                "¡Hola! Puedes obtener más información sobre nosotros a través de nuestro sitio web, redes sociales o correo electrónico. "
                "Estamos aquí para ayudarte en cualquier momento."
            )
        
        return None

    def call_gemini_api(self, message):
        """Llama a la API de Gemini y devuelve la respuesta generada."""
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            return 'Error: La clave de API no está configurada.'

        try:
            response = requests.post(
                f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}',
                headers={'Content-Type': 'application/json'},
                json={'contents': [{'parts': [{'text': message}]}]}
            )

            response.raise_for_status()  # Lanza un error para respuestas no exitosas
            return response.json().get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'Sin respuesta')
        except requests.ConnectionError:
            return 'No se pudo conectar con el servicio. Por favor, verifica tu conexión a Internet.'
        except requests.Timeout:
            return 'La solicitud ha tardado demasiado. Por favor, intenta de nuevo más tarde.'
        except requests.RequestException as e:
            return f'Error al llamar a la API: {str(e)}'

################## PARA EL ANALISIS DE DATOS ###########################################################

# views.py
from django.shortcuts import render
from .models import PalabraFrecuente  # Importa el modelo si lo creaste
from .analisis import analizar_preguntas  # Asegúrate de que la función esté disponible
import os

def estadisticas_preguntas(request):
    # Analizar las preguntas
    frecuencias = analizar_preguntas('questions_log.txt')

    # (Opcional) Guardar en la base de datos
    for palabra, frecuencia in frecuencias:
        PalabraFrecuente.objects.update_or_create(palabra=palabra, defaults={'frecuencia': frecuencia})

    # Pasar los resultados a la plantilla
    context = {
        'frecuencias': frecuencias,
    }
    return render(request, 'estadisticas.html', context)
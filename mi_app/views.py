from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, News, Comment, Reply, CustomUser_CreationForm, Image, TermsAndConditions, Services, Contact
from .forms import TermsAndConditionsForm, ServicesForm, ContactForm, ContactMessageForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
import logging
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from django.utils import translation

from django.conf import settings  # Importa settings para acceder a LANGUAGE_SESSION_KEY
from django.utils.translation import gettext as _

########## Cambio de idioma##################
# Define LANGUAGE_SESSION_KEY manualmente
LANGUAGE_SESSION_KEY = 'django_language'

# Define LANGUAGE_SESSION_KEY si no está disponible
def switch_language(request):
    lang_code = request.GET.get('lang', 'en')
    translation.activate(lang_code)
    request.session[LANGUAGE_SESSION_KEY] = lang_code  # Usa la constante directamente
    
    # Ahora obtén el idioma actual después de activarlo
    current_language = translation.get_language()
    
    print("Session content:", request.session)
    print(f"Language switched to: {lang_code}")  # Para depuración
    print("Current language:", current_language)  # Esto ahora mostrará el idioma correcto
    print(f"Current language in home view: {current_language}")

    return redirect(request.META.get('HTTP_REFERER', '/'))

# Configura el logger
logger = logging.getLogger(__name__)

def index(request):
    current_language = translation.get_language()  # Obtén el idioma actual
    return render(request, 'index.html', {
        'LANGUAGE_CODE': current_language,  # Asegúrate de pasar el idioma actual
        'request': request,  # Asegúrate de pasar el objeto de solicitud si lo necesitas
    })


def home(request):
    current_language = translation.get_language()
    articles = Article.objects.all()
    news = News.objects.all()
    images = Image.objects.all()
    comments = Comment.objects.all()  # Fetch all comments

     # Determinar si se debe mostrar el banner de cookies
    show_cookie_banner = request.COOKIES.get('cookie_consent') is None
    
    return render(request, 'home.html', {
        'articles': articles,
        'news': news,
        'comments': comments,  # Pass comments to the template
        'images': images,
        'show_cookie_banner': show_cookie_banner,  # Pasar la variable al contexto
        'LANGUAGE_CODE': current_language,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página de inicio
            return redirect('home')  # o redirect('/')
        else:
            # Mostrar mensaje de error
            messages.error(request, 'Credenciales incorrectas')
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    else:
        return redirect('home')

@csrf_protect
@login_required
def submit_comment(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_content = request.POST.get('comment')
            Comment.objects.create(user=request.user, content=comment_content)
            return redirect('home')
        else:
            
            return redirect('home')
    else:
        messages.error(request, 'Credenciales incorrectas')
        return redirect('login')

def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.likes += 1
        comment.save()
        return JsonResponse({'likes': comment.likes})

def dislike_comment(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.dislikes += 1
        comment.save()
        return JsonResponse({'dislikes': comment.dislikes})

def submit_reply(request):
    if request.method == 'POST':
        content = request.POST.get('reply')
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        reply = Reply.objects.create(user=request.user, content=content, comment=comment)
        reply.save()
        return redirect('home')  # Cambia 'home' por el nombre de la vista que desees redirigir
    return HttpResponse(status=400) 

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Asegúrate de tener esta plantilla

    def get_success_url(self):
        return reverse_lazy('home')

def register(request):
    if request.method == 'POST':
        form = CustomUser_CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f'Nuevo usuario registrado: {user.username}')  # Registra el nombre de usuario
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Por favor, corrige los errores.')
    else:
        form = CustomUser_CreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def articles_details(request, id):
    articles = Article.objects.all()  # Obtiene todos los artículos
    images = Image.objects.all()
    return render(request, 'articles_details.html', {
        'articles': articles,
        'images': images
        })

def news_details(request, id):
    news = News.objects.all()
    images = Image.objects.all() 
    return render(request, 'news_details.html', {
        'news': news,
        'images': images
        })

def about(request):
    images = Image.objects.all()
    return render(request, 'about.html',{
        'images': images
    })


def services(request):
    images = Image.objects.all()
    services = Services.objects.all()  # Obtener todos los servicios de la base de datos
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')  # Cambia esto al nombre de la vista que muestra los servicios
    else:
        form = ServicesForm()
    return render(request, 'services.html', {
        'form': form,
        'images': images,
        'services':  services
        })


def contact(request): 
    images = Image.objects.all()
    contact = Contact.objects.all()
    
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tienes un nuevo mensaje de contacto.') 
    else:
        form = ContactMessageForm()
      
    return render(request, 'contact.html', {
        'form': form,
        'images': images,
        'contact': contact,
        
    }) 

        

def terms_and_conditions_view(request):
    images = Image.objects.all()
    terms = TermsAndConditions.objects.first()  # Obtener el primer objeto
    if request.method == 'POST':
        form = TermsAndConditionsForm(request.POST, instance=terms)
        if form.is_valid():
            form.save()
            return redirect('terms_and_conditions')  # Redirigir a la misma vista
    else:
        form = TermsAndConditionsForm(instance=terms)

    return render(request, 'terms_and_conditions.html', {
        'form': form,
        'terms': terms,
        'images': images
         })

def search(request):
    images = Image.objects.all()
    query = request.GET.get('search', '')
    results = []

    if query:
        # Realiza la búsqueda en tu modelo
        results = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(created_at__icontains=query)
        )  # Ajusta el campo según tu modelo

    # Verifica si la solicitud es AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        results_data = [{'id': article.id, 'title': article.title, 'content': article.content, 'created_at': article.created_at} for article in results]
        return JsonResponse({'results': results_data})

    return render(request, 'search_results.html', {'results': results, 'query': query, 'images': images})


#################################chat IA###########################################


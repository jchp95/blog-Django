# blog/mi_app/urls.py
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

handler404 = 'mi_app.views.custom_404_view'
handler500 = 'mi_app.views.custom_500_view'

from django.contrib.auth.views import LogoutView 
from .views import (
    index,
    home,
    register,
    CustomLoginView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    submit_comment,
    like_comment,
    dislike_comment,
    submit_reply,
    articles_details,
    news_details,
    about,
    services,
    contact,
    terms_and_conditions_view,
    switch_language,
    search,
    faq_view,
    get_visitas,
    get_suscriptores, 
    incrementar_visitas, 
    incrementar_suscriptores,
    calificar  
)

urlpatterns = [ 

    path('api/visitas/', get_visitas, name='get_visitas'),
    path('api/suscriptores/', get_suscriptores, name='get_suscriptores'),
    path('api/incrementar_visitas/', incrementar_visitas, name='incrementar_visitas'),
    path('api/incrementar_suscriptores/', incrementar_suscriptores, name='incrementar_suscriptores'),
    path('api/calificar/', calificar, name='calificar'),  # Asegúrate de que la ruta sea correcta

    path('', home, name='home'),  # Vista de inicio

    path('accounts/register/', register, name='register'),  # Registro de usuario
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Cambia aquí a 'login'
    path('logout/', LogoutView.as_view(), name='logout'),  # URL para logout
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),  # Restablecer contraseña
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),  # Hecho de restablecimiento
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Confirmar restablecimiento
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Completado

    path('oauth/', include('social_django.urls', namespace='social')), 

    path('submit_comment/', submit_comment, name='submit_comment'),  # Enviar comentario
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),  # Dar like a un comentario
    path('dislike_comment/<int:comment_id>/', dislike_comment, name='dislike_comment'),  # Dar dislike a un comentario
    path('submit_reply/', submit_reply, name='submit_reply'),  # Enviar respuesta
    path('articles/<int:id>/', articles_details, name='articles_details'),  # Detalles de artículos
    path('news/<int:id>/', news_details, name='news_details'),  # Detalles de noticias
    path('about/', about, name='about'),  # Acerca de
    path('services/', services, name='services'),  # Servicios
    path('contact/', contact, name='contact'),  # Contacto
    path('terms/', terms_and_conditions_view, name='terms_and_conditions'),  # Términos y condiciones   
    path('faq/', faq_view, name='faq'),
    
    path('switch_language/', switch_language, name='switch_language'),  # Cambiar idioma
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
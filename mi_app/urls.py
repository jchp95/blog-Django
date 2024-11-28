# blog/mi_app/urls.py
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500


handler404 = 'mi_app.views.custom_404_view'
handler500 = 'mi_app.views.custom_500_view'


from .views import (
    index,
    home,
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
     
)

urlpatterns = [ 

    

    path('', home, name='home'),  # Vista de inicio

   

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
    
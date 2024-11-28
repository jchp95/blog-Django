from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from django.contrib.auth.views import LogoutView

from .views import (
    register,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    get_visitas,
    get_suscriptores, 
    incrementar_visitas, 
    incrementar_suscriptores,
    calificar 
)

handler404 = 'mi_app.views.custom_404_view'
handler500 = 'mi_app.views.custom_500_view'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  

    path('oauth/', include('social_django.urls', namespace='social')),
   
    path('register/', register, name='register'),  # Registro de usuario
    path('logout/', LogoutView.as_view(), name='logout'),  # URL para logout
    path('api/visitas/', get_visitas, name='get_visitas'),
    path('api/suscriptores/', get_suscriptores, name='get_suscriptores'),
    path('api/incrementar_visitas/', incrementar_visitas, name='incrementar_visitas'),
    path('api/incrementar_suscriptores/', incrementar_suscriptores, name='incrementar_suscriptores'),
    path('api/calificar/', calificar, name='calificar'),  # Asegúrate de que la ruta sea correcta

]
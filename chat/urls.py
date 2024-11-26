from django.urls import path
from .views import ChatResponseView, estadisticas_preguntas

urlpatterns = [
    path('chat/', ChatResponseView.as_view(), name='chat_response'),  # Usa as_view() para conectar la clase
    path('estadisticas/', estadisticas_preguntas, name='estadisticas_preguntas'),
]
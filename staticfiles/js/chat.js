document.getElementById('chat-icon').addEventListener('click', function() {
    const chatOffcanvas = document.getElementById('chatOffcanvas');
    chatOffcanvas.style.display = 'block'; // Mostrar el offcanvas
});

document.getElementById('close-chat').addEventListener('click', function() {
    const chatOffcanvas = document.getElementById('chatOffcanvas');
    chatOffcanvas.style.display = 'none'; // Ocultar el offcanvas
});

document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir el comportamiento por defecto del formulario
    const messageInput = document.getElementById('message');
    const message = messageInput.value.trim();
    if (!message) return; // No enviar mensajes vacíos

    messageInput.value = '';

    const chatContainer = document.getElementById('chat-container');
    chatContainer.innerHTML += `<div class="user-message"><strong>Tú:</strong> ${message}</div>`;

    // Obtener el token CSRF del cookie
    const csrftoken = getCookie('csrftoken');

    fetch('/chat/', {  // Asegúrate de que esta URL sea correcta
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,  // Incluir el token CSRF aquí
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(data => {
        const generatedText = data.response || data.error || 'No se recibió respuesta.';
        typeWriterEffect(generatedText); // Llama a la función para mostrar el texto letra por letra
    })
    .catch(error => {
        chatContainer.innerHTML += `<div class="assistant-message"><strong>Error:</strong> ${error.message}</div>`;
    });
});

// Función para mostrar el texto letra por letra
function typeWriterEffect(text) {
    const chatContainer = document.getElementById('chat-container');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'assistant-message';
    messageDiv.innerHTML = '<strong>Asistente:</strong> ';
    chatContainer.appendChild(messageDiv); // Agregar el div al contenedor del chat

    let index = 0;
    const speed = 20; // Velocidad de escritura en milisegundos

    function type() {
        if (index < text.length) {
            messageDiv.innerHTML += text.charAt(index);
            index++;
            setTimeout(type, speed);
        } else {
            chatContainer.scrollTop = chatContainer.scrollHeight; // Desplazar hacia abajo al final
        }
    }

    type(); // Iniciar el efecto de escritura
}

// Función para obtener el token CSRF de las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Comprobar si este cookie comienza con el nombre que buscamos
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
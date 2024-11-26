function likeComment(commentId) {
    fetch(`/like_comment/${commentId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // Asegúrate de enviar el token CSRF
        },
    })
    .then(response => response.json())
    .then(data => {
        const likeElement = document.getElementById(`like-${commentId}`);
        likeElement.innerText = `👍 ${data.likes}`; // Actualiza el número de likes
        reorderComments(); // Reorganiza los comentarios después de un like
    });
}

function dislikeComment(commentId) {
    fetch(`/dislike_comment/${commentId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // Asegúrate de enviar el token CSRF
        },
    })
    .then(response => response.json())
    .then(data => {
        const dislikeElement = document.getElementById(`dislike-${commentId}`);
        dislikeElement.innerText = `👎 ${data.dislikes}`;
    });
}

function toggleReplies(commentId) {
    const repliesContainer = document.getElementById(`replies-container-${commentId}`);
    if (repliesContainer.style.display === "none" || repliesContainer.style.display === "") {
        repliesContainer.style.display = "block"; // Muestra las respuestas
    } else {
        repliesContainer.style.display = "none"; // Oculta las respuestas
    }
}

function reorderComments() {
    const commentsContainer = document.getElementById('comments-container'); // Contenedor de comentarios
    const comments = Array.from(commentsContainer.children); // Convierte los hijos en un array

    // Ordena los comentarios de mayor a menor según la cantidad de likes
    comments.sort((a, b) => {
        const likesA = parseInt(a.querySelector('[id^="like-"]').innerText.replace('👍 ', ''));
        const likesB = parseInt(b.querySelector('[id^="like-"]').innerText.replace('👍 ', ''));
        return likesB - likesA; // Ordenar de mayor a menor
    });

    // Reinsertar los comentarios en el contenedor en el nuevo orden
    comments.forEach(comment => commentsContainer.appendChild(comment));
}

// Función para obtener el token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Si este cookie string comienza con el nombre que buscamos, recuperamos el valor
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function toggleReplyForm(commentId) {
    const replyForm = document.getElementById(`reply-form-${commentId}`);
    if (replyForm.style.display === "none") {
        replyForm.style.display = "block";
    } else {
        replyForm.style.display = "none";
    }
}


document.addEventListener('DOMContentLoaded', () => {
const cardWrapper = document.querySelector('.card-wrapper');
const cards = document.querySelectorAll('.card-slide');
const totalCards = cards.length;
const cardsToShow = 4; // Número de tarjetas a mostrar
let currentIndex = 0;


function showNextCards() {
    currentIndex += cardsToShow;

    // Si se supera el número total de tarjetas, volver al inicio
    if (currentIndex >= totalCards) {
        currentIndex = 0; // Reinicia a las primeras tarjetas
    }

    // Calcular el desplazamiento
    const cardWidth = 200; // Ancho de la tarjeta
    const cardMargin = 20; // Margen entre tarjetas
    const offset = -currentIndex * (cardWidth + cardMargin); // Ajustar el desplazamiento

    cardWrapper.style.transform = `translateX(${offset}px)`;
}

// Cambia el intervalo según lo desees (en milisegundos)
setInterval(showNextCards, 4000); // Cambia cada 3 segundos

});

// COOKIES
document.addEventListener("DOMContentLoaded", function() {
    // Esperar 3 segundos antes de mostrar el banner de cookies
    setTimeout(function() {
        if (document.getElementById('cookie-banner')) {
            document.getElementById('cookie-banner').classList.add('show');
        }
    }, 3000); // 3000 milisegundos = 3 segundos

    // Manejar el clic en el botón de aceptar cookies
    document.getElementById('accept-cookies').onclick = function() {
        document.cookie = "cookie_consent=true; path=/; max-age=" + 60*60*24*30;  // 30 días
        document.getElementById('cookie-banner').style.display = 'none';
    };

    // Manejar el clic en el botón de rechazar cookies
    document.getElementById('reject-cookies').onclick = function() {
        document.getElementById('cookie-banner').style.display = 'none';
    };
});

document.addEventListener("DOMContentLoaded", function() {
    const elements = document.querySelectorAll('.scroll-fade');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Dejar de observar el elemento una vez que es visible
            }
        });
    });

    elements.forEach(element => {
        observer.observe(element); // Comenzar a observar cada elemento
    });
});
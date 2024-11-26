// ==============================
// Inicialización de contadores
// ==============================
let visitas = 0;
let suscriptores = 0;

// Función para obtener visitas y suscriptores del servidor
async function fetchCounts() {
    try {
        const responseVisitas = await fetch('/api/visitas');
        if (!responseVisitas.ok) throw new Error('Error al obtener visitas');
        visitas = await responseVisitas.json();

        const responseSuscriptores = await fetch('/api/suscriptores');
        if (!responseSuscriptores.ok) throw new Error('Error al obtener suscriptores');
        suscriptores = await responseSuscriptores.json();

        document.getElementById('visitas').innerText = visitas;
        document.getElementById('suscriptores').innerText = suscriptores;
    } catch (error) {
        console.error('Error fetching counts:', error);
        alert('No se pudieron cargar los datos. Intenta de nuevo más tarde.');
    }
}

// ==============================
// Funciones para manejar visitas y suscriptores
// ==============================
async function incrementVisitas() {
    try {
        const response = await fetch('/api/incrementar_visitas/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Incluye el token CSRF aquí
                'Content-Type': 'application/json' // Asegúrate de incluir el tipo de contenido
            },
        });
        if (!response.ok) throw new Error('Error al incrementar visitas');
        const data = await response.json();
        console.log('Visitas incrementadas:', data);
    } catch (error) {
        console.error('Error incrementando visitas:', error);
    }
}

async function incrementSuscriptores() { 
    try {
        const response = await fetch('/api/incrementar_suscriptores', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Incluye el token CSRF aquí
                'Content-Type': 'application/json' // Asegúrate de incluir el tipo de contenido
            },
        });
        if (!response.ok) throw new Error('Error al incrementar suscriptores');
        fetchCounts(); // Actualiza la vista
    } catch (error) {
        console.error('Error incrementing suscriptores:', error);
        alert('No se pudo incrementar los suscriptores. Intenta de nuevo más tarde.');
    }
}

// ==============================
// Manejo del banner de cookies
// ==============================
function setupCookieBanner() {
    setTimeout(() => {
        const cookieBanner = document.getElementById('cookie-banner');
        if (cookieBanner) {
            cookieBanner.classList.add('show');

            const acceptCookiesButton = document.getElementById('accept-cookies');
            if (acceptCookiesButton) {
                acceptCookiesButton.onclick = function() {
                    document.cookie = "cookie_consent=true; path=/; max-age=" + 60*60*24*30;  // 30 días
                    incrementVisitas(); // Incrementa visitas al aceptar cookies
                    cookieBanner.style.display = 'none'; // Ocultar el banner
                };
            } else {
                console.error('El botón de aceptar cookies no se encontró.');
            }

            const rejectCookiesButton = document.getElementById('reject-cookies');
            if (rejectCookiesButton) {
                rejectCookiesButton.onclick = function() {
                    cookieBanner.style.display = 'none'; // Ocultar el banner
                };
            } else {
                console.error('El botón de rechazar cookies no se encontró.');
            }
        }
    }, 3000); // 3000 milisegundos = 3 segundos
}
// ==============================
// Manejo de la calificación
// ==============================
let selectedRating = 0; // Variable para almacenar la calificación seleccionada

const ratingStars = document.querySelectorAll('#rating .star');
const averageStars = document.querySelectorAll('#average-rating .s-rating'); // Asegúrate de seleccionar las estrellas correctas
const averageValueElement = document.getElementById('average-value'); // Elemento para mostrar el promedio

ratingStars.forEach(star => {
    star.addEventListener('click', () => {
        selectedRating = star.getAttribute('data-value');
        ratingStars.forEach(s => s.classList.remove('selected'));
        for (let i = 0; i < selectedRating; i++) {
            ratingStars[i].classList.add('selected');
        }
        document.getElementById('ratingResult').innerText = `Has calificado con ${selectedRating} estrella(s)`;
    });
});

document.getElementById('submitRating').addEventListener('click', async () => {
    if (selectedRating > 0) {
        try {
            const response = await fetch('/api/calificar/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ rating: selectedRating })
            });

            // Agregar un log para ver el estado y el cuerpo de la respuesta
            console.log('Response Status:', response.status);
            const data = await response.json(); // Llama a json una vez
            console.log('Response Body:', data); // Log del cuerpo de la respuesta

            if (!response.ok) throw new Error('Error al enviar la calificación');

            // Actualiza el promedio mostrado en estrellas
            displayAverageRating(data.average);
            document.getElementById('ratingResult').innerText += ' - Calificación enviada con éxito!';
        } catch (error) {
            console.error('Error enviando calificación:', error);
            alert('No se pudo enviar la calificación. Intenta de nuevo más tarde.');
        }
    } else {
        document.getElementById('ratingResult').innerText = 'Por favor selecciona una calificación';
    }
});

// Función para mostrar el promedio de calificaciones en forma de estrellas
function displayAverageRating(average) {
    averageValueElement.innerText = average; // Actualiza el valor promedio en el DOM

    // Selecciona todas las estrellas para el promedio
    averageStars.forEach(star => {
        star.classList.remove('filled'); // Limpia las estrellas llenas
        // Corregido: eliminar el espacio en 'data-value'
        if (parseFloat(star.getAttribute('data-value')) <= average) {
            star.classList.add('filled'); // Rellena las estrellas según el promedio
        }
    });
}

// Llama a esta función cuando se cargue la página para mostrar el promedio inicial
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/api/calificar/'); // Asegúrate de tener un endpoint para obtener el promedio
        const data = await response.json();
        if (data.average) {
            displayAverageRating(data.average);
        }
    } catch (error) {
        console.error('Error al obtener el promedio de calificaciones:', error);
    }
});
// ==============================
// Manejo de comentarios
// ==============================
function likeComment(commentId) {
    fetch(`/like_comment/${commentId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
    .then(response => response.json())
    .then(data => {
        const likeElement = document.getElementById(`like-${commentId}`);
        likeElement.innerText = `👍 ${data.likes}`;
        reorderComments();
    });
}

function dislikeComment(commentId) {
    fetch(`/dislike_comment/${commentId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
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
        repliesContainer.style.display = "block";
    } else {
        repliesContainer.style.display = "none";
    }
}

function reorderComments() {
    const commentsContainer = document.getElementById('comments-container');
    const comments = Array.from(commentsContainer.children);

    comments.sort((a, b) => {
        const likesA = parseInt(a.querySelector('[id^="like-"]').innerText.replace('👍 ', ''));
        const likesB = parseInt(b.querySelector('[id^="like-"]').innerText.replace('👍 ', ''));
        return likesB - likesA;
    });

    comments.forEach(comment => commentsContainer.appendChild(comment));
}

function toggleReplyForm(commentId) {
    const replyForm = document.getElementById(`reply-form-${commentId}`);
    if (replyForm.style.display === "none") {
        replyForm.style.display = "block";
    } else {
        replyForm.style.display = "none";
    }
}

// ==============================
// Inicialización del carrusel de tarjetas
// ==============================
const cardWrapper = document.querySelector('.card-wrapper');
const cards = document.querySelectorAll('.card-slide');
const totalCards = cards.length;
const cardsToShow = 4;
let currentIndex = 0;

function showNextCards() {
    currentIndex += cardsToShow;

    if (currentIndex >= totalCards) {
        currentIndex = 0;
    }

    const cardWidth = 200;
    const cardMargin = 20;
    const offset = -currentIndex * (cardWidth + cardMargin);

    cardWrapper.style.transform = `translateX(${offset}px)`;
}

setInterval(showNextCards, 4000);

// ==============================
// Manejo de elementos que se desvanecen al hacer scroll
// ==============================
const elements = document.querySelectorAll('.scroll-fade');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
});

elements.forEach(element => {
    observer.observe(element);
});

// ==============================
// Evento de carga de la página
// ==============================
document.addEventListener('DOMContentLoaded', () => {
    fetchCounts();
    setupCookieBanner();
});

// ==============================
// Función para obtener el token CSRF
// ==============================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
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
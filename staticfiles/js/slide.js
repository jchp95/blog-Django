document.addEventListener('DOMContentLoaded', () => {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.card-slide');
    const totalSlides = slides.length;
    const slidesToShow = 4; // Muestra 4 tarjetas a la vez
    const slidesToMove = 4; // Mueve 4 tarjetas a la vez

    function showSlide(index) {
        const offset = index * -(100 / (totalSlides / slidesToShow)); // Calcula la traslación en función de cuántas tarjetas muestras
        document.querySelector('.slide-container').style.transform = `translateX(${offset}%)`;
    }

    // Cambia el tiempo de deslizamiento a 10 segundos (10000 milisegundos)
    setInterval(() => {
        currentIndex = (currentIndex + slidesToMove) % Math.ceil(totalSlides / slidesToMove); // Asegúrate de no superar el número de "sets" de tarjetas
        showSlide(currentIndex);
    }, 10000); // Cambia de slide cada 10 segundos

    // Funciones para los botones de navegación
    document.querySelector('.next').addEventListener('click', () => {
        currentIndex = (currentIndex + slidesToMove) % Math.ceil(totalSlides / slidesToMove); // Avanza al siguiente set
        showSlide(currentIndex);
    });

    document.querySelector('.prev').addEventListener('click', () => {
        currentIndex = (currentIndex - slidesToMove + Math.ceil(totalSlides / slidesToMove)) % Math.ceil(totalSlides / slidesToMove); // Retrocede al set anterior
        showSlide(currentIndex);
    });
});



// search.js
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-input');
    const resultsContainer = document.querySelector('.search-results'); // Asegúrate de que este elemento exista en tu HTML

    searchInput.addEventListener('input', function() {
        const query = searchInput.value;

        if (query.length > 2) { // Solo buscar si hay más de 2 caracteres
            fetch(`/search/?search=${query}`)
                .then(response => response.json())
                .then(data => {
                    resultsContainer.innerHTML = ''; // Limpiar resultados previos

                    if (data.results.length > 0) {
                        data.results.forEach(result => {
                            const resultItem = document.createElement('div');
                            resultItem.classList.add('result-item'); // Añade una clase para estilizar si es necesario
                            resultItem.innerHTML = `
                                <h3>${result.title}</h3>
                                <p>${result.content}</p>
                                <small>Created on: ${new Date(result.created_at).toLocaleDateString()}</small>
                            `; // Muestra el título, contenido y la fecha de creación
                            resultsContainer.appendChild(resultItem);
                        });
                    } else {
                        resultsContainer.innerHTML = '<p>No se encontraron resultados.</p>';
                    }
                })
                .catch(error => console.error('Error:', error));
        } else {
            resultsContainer.innerHTML = ''; // Limpiar resultados si hay menos de 3 caracteres
        }
    });
});




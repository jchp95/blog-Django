document.addEventListener('DOMContentLoaded', () => {
    const myForm = document.getElementById('myForm');
    
    if (myForm) { // Verifica que el formulario existe
        form.addEventListener('submit', function(event) {
            // Evita que el formulario se envíe inmediatamente
            event.preventDefault();

            // Obtener todos los campos del formulario
            const formElements = Array.from(this.elements);
            const allFieldsFilled = formElements.every(element => 
                element.type === "submit" || element.value
            );

            // Si todos los campos están llenos, mostrar la alerta
            if (allFieldsFilled) {
                Swal.fire({
                    position: "top-center",
                    icon: "success",
                    title: "Tu mensaje se ha enviado con éxito",
                    showConfirmButton: false,
                    timer: 2500
                }).then(() => {
                    this.submit(); // Submit after the alert
                });
            } else {
                // Si no todos los campos están llenos, mostrar un mensaje de error
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Por favor, completa todos los campos del formulario.'
                });
            }
        });
    } else {
        console.error("El formulario con ID 'myForm' no se encontró en el DOM.");
    }
});
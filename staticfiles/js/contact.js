document.getElementById('myForm').addEventListener('submit', function(event) {
    // Evita que el formulario se envíe inmediatamente
    event.preventDefault();

    // Obtener todos los campos del formulario
    const formElements = this.elements;
    let allFieldsFilled = true;

    // Verificar si todos los campos están llenos
    for (let i = 0; i < formElements.length; i++) {
        if (formElements[i].type !== "submit" && !formElements[i].value) {
            allFieldsFilled = false;
            break;
        }
    }

    // Si todos los campos están llenos, mostrar la alerta
    if (allFieldsFilled) {
        Swal.fire({
            position: "top-center",
            icon: "success",
            title: "Tu mensaje se ha enviado con éxito",
            showConfirmButton: false, // Muestra el botón de confirmación
            timer: 2500 // Temporizador de 3 segundos
        }).then((result) => {
            if (result.isConfirmed) {
                // Si el usuario hace clic en el botón de confirmación, se envía el formulario
                this.submit();
            } else {
                // Si no, se envía el formulario automáticamente después de 3 segundos
                this.submit();
            }
        });
    } else {
        // Si no todos los campos están llenos, puedes mostrar un mensaje de error
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Por favor, completa todos los campos del formulario.'
        });
    }
});
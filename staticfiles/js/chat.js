  const chatContainer = document.getElementById('chat-container');
        const chatToggle = document.getElementById('chat-toggle');

        chatToggle.addEventListener('click', () => {
            if (chatContainer.style.display === 'none' || chatContainer.style.display === '') {
                chatContainer.style.display = 'block'; // Mostrar el chat
            } else {
                chatContainer.style.display = 'none'; // Ocultar el chat
            }
        });
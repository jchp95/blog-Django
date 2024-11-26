from bs4 import BeautifulSoup

# Función para analizar el HTML y verificar SEO
def verificar_seo(html_content, palabras_clave):
    # Analizar el contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Verificar el título
    title = soup.title.string if soup.title else 'Sin título'
    print("Título:", title)
    verificar_palabra_clave(title, palabras_clave)

    # Verificar la descripción
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if meta_description:
        description_content = meta_description['content']
        print("Descripción:", description_content)
        verificar_palabra_clave(description_content, palabras_clave)
    else:
        print("No se encontró la meta descripción.")

    # Verificar encabezados
    for i in range(1, 7):  # Para h1 a h6
        encabezados = soup.find_all(f'h{i}')
        for encabezado in encabezados:
            print(f"Encabezado h{i}:", encabezado.text)
            verificar_palabra_clave(encabezado.text, palabras_clave)

# Función para verificar si las palabras clave están presentes
def verificar_palabra_clave(texto, palabras_clave):
    for palabra in palabras_clave:
        if palabra.lower() in texto.lower():
            print(f"✔️ La palabra clave '{palabra}' está presente en: {texto}")
        else:
            print(f"❌ La palabra clave '{palabra}' NO está presente en: {texto}")

# Ejemplo de uso
if __name__ == "__main__":
    # Aquí debes poner el contenido HTML que deseas analizar
    html_content = """{% load static %}

 <!--New Section for SLIDE-->
<div class="container-slide-section">
    <div class="slide-section">
        <div class="slide-container">
            <div class="card-wrapper"> 
                {% for image in images %}
                    <div class="card-slide">
                        <img src="{{ image.image.url }}" alt="Imagen" class="card-image-slide">
                        <div class="card-content-slide">
                            <h3 class="card-title-slide">{{ image.title }}</h3>
                            <p class="card-description-slide">{{ image.description }}</p>
                            <a href="{{ image.link }}" target="_blank" class="link-card-slide">get it here</a>
                        </div>
                    </div>
                {% empty %}
                    <p>No images available..</p>
                {% endfor %}
            </div>
        </div>
      
    </div>
      <!-- Botones de navegación -->
      <button class="prev">Prev</button>
      <button class="next">Next</button>
</div>


    """

    # Lista de palabras clave que deseas verificar
    palabras_clave = ["remote work", "flexibility", "available courses", "commit"]

    # Llamar a la función de verificación
    verificar_seo(html_content, palabras_clave)

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import re

# Agregar la ruta a nltk_data
nltk.data.path.append('nltk_data')  # Cambia esto a la ruta correcta

def analizar_preguntas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        preguntas = file.readlines()

    # Unir todas las preguntas en un solo texto
    texto = ' '.join(preguntas)

    # Limpiar el texto: eliminar caracteres especiales y poner en minúsculas
    texto = re.sub(r'[^\w\s]', '', texto.lower())

    # Tokenizar el texto
    palabras = word_tokenize(texto)

    # Eliminar stop words
    stop_words = set(stopwords.words('spanish'))  # Cambia a 'english' si usas inglés
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]

    # Lematizar las palabras
    lemmatizer = WordNetLemmatizer()
    palabras_lemmatizadas = [lemmatizer.lemmatize(palabra) for palabra in palabras_filtradas]

    # Contar la frecuencia de cada palabra
    contador = Counter(palabras_lemmatizadas)

    # Obtener las 10 palabras más comunes
    palabras_comunes = contador.most_common(10)

    return palabras_comunes

# Llamada a la función
frecuencias = analizar_preguntas('questions_log.txt')
print(frecuencias)
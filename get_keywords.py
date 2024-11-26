import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
import csv
import pandas as pd
import matplotlib.pyplot as plt
import re

# Función para obtener el contenido de una página web
def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error para códigos de estado 4xx y 5xx
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la página: {e}")
        return None

# Función para extraer palabras clave
def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    keywords_with_scores = rake.get_ranked_phrases_with_scores()
    return keywords_with_scores

# Función para limpiar y guardar palabras clave en un archivo CSV
def save_keywords_to_csv(keywords, filename='keywords.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Phrase', 'Score'])
        for score, phrase in keywords:
            cleaned_phrase = remove_emojis(phrase.strip())  # Limpiar la frase de emojis y espacios
            writer.writerow([cleaned_phrase, score])
    print(f"Palabras clave guardadas en {filename}")

# Función para eliminar emojis
def remove_emojis(text):
    emoji_pattern = re.compile("[\U0001F600-\U0001F64F"
                                "\U0001F300-\U0001F5FF"
                                "\U0001F680-\U0001F6FF"
                                "\U0001F700-\U0001F77F"
                                "\U0001F780-\U0001F7FF"
                                "\U0001F800-\U0001F8FF"
                                "\U0001F900-\U0001F9FF"
                                "\U0001FA00-\U0001FA6F"
                                "\U00002700-\U000027BF"
                                "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Función para eliminar duplicados en el archivo CSV
def remove_duplicates_in_csv(csv_file_path):
    data = pd.read_csv(csv_file_path)
    data = data.drop_duplicates(subset='Phrase')
    data.to_csv(csv_file_path, index=False)

# URL del sitio web que deseas analizar
url = 'https://elblog.onrender.com/'

# Obtener el contenido de la página
page_content = get_page_content(url)

# Inicializar keywords
keywords = []

if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text()
    keywords = extract_keywords(text)

if keywords:
    keywords.sort(reverse=True, key=lambda x: x[0])
    
    for score, phrase in keywords:
        print(f'{phrase}: {score}')
    
    save_keywords_to_csv(keywords)
    remove_duplicates_in_csv('keywords.csv')
else:
    print("No se encontraron palabras clave.")

# --- Análisis del archivo CSV ---

file_path = 'keywords.csv'
data = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
print(data.head())

# Filtrar palabras clave con un score mayor a 10
filtered_data = data[data['Score'] > 10].copy()  # Crear una copia del DataFrame para evitar el SettingWithCopyWarning
filtered_data.loc[:, 'Phrase'] = filtered_data['Phrase'].apply(remove_emojis)  # Usar .loc[] para evitar advertencias

# Mostrar el DataFrame filtrado
print(filtered_data)

# Visualizar la distribución de las puntuaciones
plt.figure(figsize=(10, 6))
plt.barh(filtered_data['Phrase'], filtered_data['Score'], color='skyblue')
plt.xlabel('Score')
plt.title('Distribución de Palabras Clave')
plt.show()
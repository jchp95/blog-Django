import os
from collections import defaultdict

# Cambia esta ruta a la ruta de tu proyecto
project_path = 'C:/Users/julio/Desktop/blog'

# Crear un diccionario para almacenar las rutas de los archivos
file_paths = defaultdict(list)

# Recorrer el directorio
for dirpath, _, filenames in os.walk(project_path):
    for filename in filenames:
        file_paths[filename].append(os.path.join(dirpath, filename))

# Mostrar archivos duplicados
for filename, paths in file_paths.items():
    if len(paths) > 1:
        print(f"Archivo duplicado: {filename}")
        for path in paths:
            print(f" - {path}")
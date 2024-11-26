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

# Lista de archivos a eliminar
files_to_delete = []

# Mostrar archivos duplicados y preparar la lista de eliminación
for filename, paths in file_paths.items():
    if len(paths) > 1:
        print(f"Archivo duplicado: {filename}")
        for path in paths[1:]:  # Mantener el primero y eliminar los demás
            print(f" - {path}")
            files_to_delete.append(path)

# Eliminar archivos duplicados
for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"Eliminado: {file_path}")
    except Exception as e:
        print(f"No se pudo eliminar {file_path}: {e}")
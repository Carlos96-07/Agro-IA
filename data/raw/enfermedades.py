import data.raw.enfermedades as enfermedades
import shutil
import os

# Descargar el dataset
print("Descargando el dataset...")
dataset_path = enfermedades.dataset_download("emmarex/plantdisease")
print("Dataset descargado en:", dataset_path)

# Ruta destino en tu proyecto
dest_path = os.path.join("data", "raw", "enfermedades")

# Crear carpeta destino si no existe
os.makedirs(dest_path, exist_ok=True)

# Copiar todo a tu estructura de proyecto
print("Moviendo archivos a:", dest_path)
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        src_file = os.path.join(root, file)
        rel_path = os.path.relpath(src_file, dataset_path)
        dst_file = os.path.join(dest_path, rel_path)

        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        shutil.copy2(src_file, dst_file)

print("Dataset listo en: data/raw/enfermedades/")

# Usa una imagen base de Python "dev" con Alpine Linux
FROM python:3.11.6-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Copia todo el contenido de la carpeta actual al directorio /app en el contenedor
COPY . .

# Instala las dependencias desde el archivo requirements.txt
RUN pip install -r requirements.txt

# Define el comando para ejecutar tu aplicación (puedes modificarlo según tu necesidad)
CMD ["python", "app.py"]


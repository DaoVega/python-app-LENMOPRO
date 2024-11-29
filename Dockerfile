# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Definir el comando para ejecutar la app
CMD ["python", "app.py"]

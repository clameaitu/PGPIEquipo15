# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app/

# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python myshop/manage.py collectstatic --noinput
# Expone el puerto 8000 (el predeterminado de Django)
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "myshop/manage.py", "runserver", "0.0.0.0:8000"]

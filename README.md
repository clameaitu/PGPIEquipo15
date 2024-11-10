# Pasos variados que nos puedan hacer falta

### Para el entorno virtual
```
python -m venv venv             # para crearlo
venv\Scripts\activate           # para activarlo (las barras hacia la izquierda)
deactivate                      # para desactivarlo
```

### Para las dependencias:
Para instalar todas (en principio debería de funcionar):
```
pip install -r requirements.txt
```

Si no, por partes:
```
pip install Django
pip install Pillow
# ...
```

Para actualizar el requirements.txt con las dependencias que se tengan en el momento:
```
pip freeze > requirements.txt
```

### Para hacer las migraciones cada vez que añadamos algún modelo:
```
python myshop\manage.py migrate
```

### Para lanzar la aplicación:
```
python myshop\manage.py runserver
```

### Administrador
Para acceder al administrador: ```http://127.0.0.1:8000/admin/```

Credenciales de administrador:
 - **Username**: ```admin```
 - **Password**: ```admin```

# Pasos variados que nos puedan hacer falta

### Para el entorno virtual
```
python -m venv venv             # para crearlo
venv\Scripts\activate           # para activarlo (las barras hacia la izquierda)
deactivate                      # para desactivarlo
```

### Para las dependencias:
Para instalar todas:
```
pip install -r requirements.txt
```

Si no, por partes:
```
pip install Django
pip install Pillow
# ...
```

Para actualizar el requirements.txt con más dependencias:
```
pip freeze > requirements.txt
```

### Para lanzar la aplicación y lo que sea:
```
python myshop\manage.py migrate
python myshop\manage.py runserver    # éste es para lanzarla seguro
```

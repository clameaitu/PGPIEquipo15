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
Cuando has cambiado un modelo, para generar las nuevas migraciones:
```
python myshop\manage.py makemigrations
```

Para aplicar nuevas migraciones:
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


### Tests
Para lanzar todos los tests (NO FUNCIONA, no te los encuentra):
```
python myshop\manage.py test
```

Para lanzar los tests de una sola app (cart, shop, orders, etc.):
```
python myshop\manage.py test <nombre_de_app>
```

Para lanzar los tests de una sola clase:
```
python myshop\manage.py test <nombre_de_app>.tests.<NombreClase>
```

Para lanzar los tests de un solo método (test):
```
python myshop\manage.py test <nombre_de_app>.tests.<NombreClase>.<nombre_de_método>
```
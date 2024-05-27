#Crea el entorno virtual para windows

```
python -m venv env
.\env\Scripts\activate
```

#Instala django

```
pip install django
```

#Ejecuta los comandos para crear las tablas

```
python manage.py makemigrations
python manage.py migrate
```

#Corre el servidor

```
python manage.py runserver
```

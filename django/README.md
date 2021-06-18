Django ORM Python Script
========================

El ORM (Object-relational mapping) de Django es una herramienta poderosa y muy versátil. En este ejemplo mostraré como usar este componente desde un script python que haga uso de una base de datos.


Requerimientos
--------------
El sistema debe tener una instalación de django existente para que podamos 
importar de forma segura los módulos necesarios. 
No se requiere una aplicación django. Entre otros requisitos está el backend db. 
Si planea usar mysql o pgsql, asegúrese de que se cumplan todas las dependencias. 
Este código funciona en Django 2.x (no lo probé con versiones anteriores).


Estructura de la aplicación
---------------------------
+ __settings.py__ - Módulo de configuración de Django (contiene la configuración de la base de datos)
+ __manage.py__ - Script principal de los proyectos django
+ __main.py__ - Nuestro código ... este es solo un archivo de muestra para demostrar cómo importar modelos
+ __data__ - El directorio de datos funciona como una aplicación django y contiene 'models.py' dónde colocaremos nuestro modelos de datos


Instalación
-----------
+ Clonamos el repositorio github
+ Creamos el environment de Python3: `python3 -m venv .env`
+ Activamos el virtualenv: `source .env/bin/activate`
+ Instalamos Django: `pip install django`


Prueba
------
+ Ejecutamos `python manage.py makemigrations` para crear las migraciones
+ Ejecutamos `python manage.py migrate` para sincronizar la base de datos y crear las tablas necesarias
+ Realizar estas acciones cada vez que modifiquemos el modelo de datos


Carga da datos iniciales
------------------------
+ Ejecutamos el script main.py para cargar datos de ejemplo `python ejemplo.py`

Se plantea el seguimiento de un curso de Django
Crear un entorno <=== python -m venv entorno
Instalar django <= Dentro del entorno se ejecuta pip install django
Para activar el entorno, se navega a la carpeta scripts y se ejecuta el activate
Crear un nuevo proyecto <= django-admin startproject nombreProyecto
Ejecutar nuestro proyecto <= python manage.py runserver
Para ejecutar nuestro proyecto en otro entorno ya sea el de produccion, testeo o el local pues se realiza lo siguiente:
python manage.py runserver --settings=empleado.settings.local (se especifica la ruta de donde está nuestro entorno)
Sin embargo para agilizar lo que se puede hacer es  configurar el manage.py para que se ejecute automáticamente el entorno que deseamos
y una vez hecho esto solo es necesario el python manage.py runserver
Para crear una aplicacion <== python manage.py startapp nombreAplicacion y si no estoy en la misma carpeta que el manage.py
pues lo que se usa es django-admin startapp (nombre de la aplicacion)



==================================================================
El archivo init.py se usa para indicar a Django cuales son los archivos/carpeta que debe leer
El archivo asgi.py es como un enlace para que python pueda levantar el servidor
El archivo settings.py es un archivo de configuración donde habrán rutas, bases de datos , etc.
El archivo urls.py es para indicar los paths que va a tener nuestro proyecto
El archivo wsgi.py es como una herramienta que nos ayuda a ejecutar correctamente nuestro servidor

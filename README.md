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
- TemplateView es únicamente para mostrar pantallas HTML directamente, es decir para apariencia.
- Haciendo referencia a los modelos pues Django usa ORM es decir Django transforma automaticamente el código a SQL por ello
en los modelos unicamente escribiremos codigo python.
- Si yo quiero que una tabla/modelo que hago en mi models.py se cree o se vea reflejado en mi bd pues ejecuto: python manage.py makemigrations y Django detectara si hay cambios y si estoy conforme con los mismos ejecuto:
python manage.py migrate
- Para poder ver que se ha creado una tabla en mi bd Django lo que ofrece es el archivo de admin.py, en el cual podemos tener  una interfaz
que nos permite interactuar con nuestra BD

- Para crearme un superusuario junto con su password para la administración de Django ejecuto lo siguiente <= python manage  createsuperuser

- Django entiende que ya todas las tablas de una BD ya tiene una primary key por lo que la crea internamente
- Instalar Ckeditor <== pip install django-ckeditor

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
Django Model Utils (para no repetir codigo en los modelos) <==pip install django-model-utils

python manage.py migrate -- fake <= Falsa migracion, nos sirve cuando los modelos ya estan creados y hemos reestrcturado nuestro proyecto pero queremos migrar y evitamos el error

========================================================
Django REST Framework ==> pip install djangorestframework

En caso de que obtener el error django.db.utils.ProgrammingError: relation does not exist LINE 1 
revisar si estan las carpetas migrations en cada app

- Para ver los paquetes instalados en mi entorno local uso pip freeze --local
- Para instalar los paquetes desde el txt uso: pip install -r .\local.txt

Anexos:
https://ccbv.co.uk/
https://docs.djangoproject.com/en/3.0/ref/models/querysets/ <= ORM Django
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#annotate <= Annotate Documentacion
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#aggregate <= Aggregate Documentacion
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id5 <= Funciones Aritméticas en el Aggregate
https://docs.djangoproject.com/en/3.0/ref/models/database-functions/ <= Aritmética ORM django

https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/search/#trigram-similarity <= Trigram Similarity

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
- Recordar que el Navegador es el cliente y nuestro software esta en un servidor alojado el cual esta recibiendo solicitudes o peticiones
- Los proyectos del curso se trabajaran con el  framework Foundation para dar estilo
- Los archivos estáticos ayudan a que nuestro HTML se pinte mejor y son archivos estaticos ya que no cambian, es decir que su valor que se ha
traído inicialmente cuando ha hecho la consulta a nuestro navegador a nuestro servidor, ese valor sera el mismo durante todo el ciclo de vida de nuestro proyecto

- Diferencia entre Include y Extends
* Extends  se podría considerar herencia, mientras que include es solamente una herramienta para organizar mejor nuestro html y no repetir código que en muchos casos es repetitivo.

* Extends en cambio es el envoltorio del html como si fuera un marco que contendrá uno o varios bloques html dentro, es decir extends hará que el código que tenga envuelva a lo que contendra.  (extends contiene bloques html)

* Include se agrega dentro de bloques, podríamos decir que a include lo contienen los bloques html.

* extends involucra que queremos trabajar bajo una maqueta o bajo una estructura de la cual estamos extendiendo, imagina que creamos una estructura base una vez analizado nuestro proyecto, y en todos los template que deban trabajar bajo esa estructura base usamos extends.

* Include son bloques HTML que podemos reutilizar en cualquier otro template, generalmente es bloque html que no siempre ira en la misma parte de la pagina, en un templete puede ir en el centro, en otro en el footer, en otro a la izquierda... pero como se repite el mismo bloque de código es mejor reutilizar código usando un includ

- Dentro de la carpeta includes estarán bloques HTML de todo nuestro sistema de templates, los cuales podremos reutilizar 

- Para la navegacion entre paginas es recomendable usar los name y no el link directo
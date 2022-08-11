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
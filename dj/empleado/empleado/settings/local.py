# Aqui va la configuracion de mi entorno local
from .base import*
# SECURITY WARNING: don't run with debug turned on in production!
#Con esto  indico que estoy en un entorno de desarrollo y no en un entorno de produccion
DEBUG = True

ALLOWED_HOSTS = []

#Pongo la base ya que se trabajará con una propia y no con una de producción
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'dbempleado',
        'USER': 'adrian',
        'PASSWORD': 'django',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

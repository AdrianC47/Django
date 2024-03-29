# Aqui va la configuracion de mi entorno local
from .base import*
# SECURITY WARNING: don't run with debug turned on in production!
#Con esto  indico que estoy en un entorno de desarrollo y no en un entorno de produccion
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("USER"),
        'PASSWORD': get_secret("PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']#Dentro de mi directorio base busco mi carpeta static

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# EMAIL SETTINGS 

EMAIL_USE_TLS = True # Se activa el envio de email con Djang
EMAIL_HOST = 'smtp.gmail.com' # SMTP
EMAIL_HOST_USER = get_secret("EMAIL")#Correo que va a abrir el email
EMAIL_HOST_PASSWORD = get_secret("PASS_EMAIL")
EMAIL_PORT = '587'    # PUERTO 
#https://www.youtube.com/watch?v=RpSQQIGTpTM


 
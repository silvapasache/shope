from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbventas',
        'USER':'neunapp',
        'PASSWORD':'neunappcursopro',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= BASE_DIR +'\statict'
STATICFILES_DIRS=[BASE_DIR.child('static')]


MEDIA_URL='/media/'
MEDIA_ROOT=BASE_DIR.child('media')
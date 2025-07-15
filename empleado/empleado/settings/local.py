from .base import *
from pathlib import Path
import os 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.0', '127.0.0.1',]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sge-django',
        'USER': 'luisloa',
        'PASSWORD': '79791313',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [ BASE_DIR / "static"]


STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

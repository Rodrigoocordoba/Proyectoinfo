# SECURITY WARNING: keep the secret key used in production secret!
from .base import *

SECRET_KEY = 'django-insecure-v-)+)b4@sdzvrmzf+9dfd++4k1=d2j9banaq2zvs2qe-kgbm4d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
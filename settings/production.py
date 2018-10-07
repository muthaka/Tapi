from base import *
from decouple import config

DEBUG = False
SECRET_KEY=config("SECRET_KEY")

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('dev_name'),
        'USER': config('dev_username'),
        'PASSWORD': config('dev_password'),
        'HOST': config('dev_host'),
        'PORT': 5432,
    }
}

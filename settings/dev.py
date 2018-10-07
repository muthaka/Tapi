from base import *
from decouple import config as c

DEBUG = True
SECRET_KEY=c("SECRET_KEY")

ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': c('dev_name'),
        'USER': c('dev_username'),
        'PASSWORD': c('dev_password'),
        'HOST': c('dev_host'),
        'PORT': 5432,
    }
}

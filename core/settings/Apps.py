SECRET_KEY = 'django-insecure-teuvq7wkkf_9^l8*90d3@^wl5%i+v58*h)9uxrr0xk$8d8pt+m'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
    'contact',
]

WSGI_APPLICATION = 'core.wsgi.application'
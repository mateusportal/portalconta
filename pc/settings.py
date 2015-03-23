# coding: utf-8
# heroku git:remote -a portalconta

import os
import cloudinary
from dj_database_url import parse as db_url
from unipath import Path

BASE_DIR = Path(__file__).parent

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/central/'

AUTH_USER_MODEL = 'empresas.Usuario'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'south',
    'pagination',
    'empresas',
    'contas',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

MAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_PORT = 587

EMAIL_USE_TLS = True

ROOT_URLCONF = 'pc.urls'

WSGI_APPLICATION = 'pc.wsgi.application'

# Tutorial: http://cloudinary.com/documentation/django_integration#getting_started_guide
if 'PRODUCTION' in os.environ:
    DEBUG = False
    TEMPLATE_DEBUG = False
    DATABASES = { 'default': dj_database_url.config(default=os.environ.get('DATABASE_URL')) }
    SECRET_KEY = os.environ.get('CONF_SECRET_KEY')
    EMAIL_HOST = os.environ.get('CONF_EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('CONF_EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('CONF_EMAIL_HOST_PASSWORD')
    cloudinary.config(
        cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key = os.environ.get('CLOUDINARY_API_KEY'),
        api_secret = os.environ.get('CLOUDINARY_API_SECRET')
    )
else:
    from settings_conf import *
    DEBUG = True
    TEMPLATE_DEBUG = True
    SECRET_KEY = CONF_SECRET_KEY
    EMAIL_HOST = CONF_EMAIL_HOST
    EMAIL_HOST_USER = CONF_EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = CONF_EMAIL_HOST_PASSWORD
    DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}
    cloudinary.config(
        cloud_name = CLOUDINARY_CLOUD_NAME,
        api_key = CLOUDINARY_API_KEY,
        api_secret = CLOUDINARY_API_SECRET
    )

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# MANUAL PARA GERAÇÃO DAS TRADUÇÕES
# django-admin.py makemessages -l pt-br
# django-admin.py compilemessages -l pt-br

LANGUAGE = (
    ('pt-br', u'Portugês'),
    ('en-us', u'English'),
    ('es', u'Español'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '../core/locale'),
)

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../core/static'),
)

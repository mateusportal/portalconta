# coding: utf-8
# ADICIONANDO HOSPEDAGEM: heroku git:remote -a portalconta
# ADICIONANDO NOVO USUARIO CASO O SOUTH NAO CRIE: python manage.py createsuperuser
# COMANDO SOUTH: python manage.py schemamigration core --auto
# COMANDO SOUTH: python manage.py migrate empresas
# APPS DO SISTEMA PARA RODAR OS COMANDOS: core empresas contas
# RODANDO MIGRATE NO HEROKU: heroku run python manage.py migrate core
# OU ESTE PARA AJUSTAR MIGRAÇÃO EM CASO DE ERROS: heroku run python manage.py migrate core --fake
# DESCOBRIR ERROS NO SERVIDOR HEROKU: heroku run python ./manage.py collectstatic --noinput
# LIMPAR BANCO HEROKU: heroku pg:reset DATABASE
# CRIAR NOVAMENTE O BANCO REMOTO: heroku run python manage.py syncdb
# RODAR O HEROKU LOCAL
# use o comando "foremans" = http://elweb.co/how-to-fix-foremans-missing-output-issue-on-python-projects/

import os
import cloudinary
import dj_database_url
from unipath import Path

BASE_DIR = Path(__file__).parent

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/sistema/'

AUTH_USER_MODEL = 'empresas.Usuario'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'cloudinary',
    'south',
    'pagination',
    'core',
    'empresas',
    'contas',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_PORT = 587

EMAIL_USE_TLS = True

ROOT_URLCONF = 'pc.urls'

WSGI_APPLICATION = 'pc.wsgi.application'

# Tutorial: http://cloudinary.com/documentation/django_integration#getting_started_guide
if 'PRODUCTION' in os.environ:
    DEBUG = True
    TEMPLATE_DEBUG = True
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

# MANUAL PARA GERAÇÃO DAS TRADUÇÕES (ENTRAR NO DIRETORIO CORE E RODAR O COMANDO)
# django-admin.py makemessages -l en  (PARA CADA LINGUA en & es)
# traduzir as mensagens do arquivo *.po
# django-admin.py compilemessages (PARA TODAS AS LINGUAS)

LANGUAGE = (
    ('pt-br', u'Portugês'),
    ('en', u'English'),
    ('es', u'Español'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '../core/locale'),
)

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

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

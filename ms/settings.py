"""
Django settings for ms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# To use a custom, extended user model
# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*&b&o-n2h#k)c^k1-uk(=0spgk9#hnu#&ccgh&6++$(!g7aawu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

template_dir = "/var/www/ms/templates"
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), template_dir).replace('\\', '/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django_facebook.context_processors.facebook',
)

AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)


FACEBOOK_APP_ID = '835081286539104'
FACEBOOK_APP_SECRET = 'd46316f391d867ff159ca98814f9865c'

FACEBOOK_LOGIN_DEFAULT_REDIRECT = '/user/home/'

AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
AUTH_PROFILE_MODEL = 'django_facebook.FacebookProfile'

logger = logging.getLogger(__name__)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'ms',
    'users',
    'comm',
    'django_facebook',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ms.urls'

WSGI_APPLICATION = 'ms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': './db.cnf',
            'init_command': 'SET foreign_key_checks = 0;',
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = '/var/www/ms/ms/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/www/ms/ms/static/'
STATIC_URL = '/static/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django_facebook': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
        },
        'open_facebook.api': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
        },
        'facebook.request': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
        },
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'INFO',
        },
    },
}

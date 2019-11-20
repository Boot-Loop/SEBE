"""
Django settings for SEBE project.

Generated by 'django-admin startproject' using Django 2.2.6
in pytonanywhere.com using Django 2.1

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


from .core import _credentials

EMAIL_USE_TLS       = True
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = _credentials.email_host_user
EMAIL_HOST_PASSWORD = _credentials.email_host_password
EMAIL_PORT          = 587

## DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
## EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
## SERVER_EMAIL        = EMAIL_HOST_USER 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _credentials.secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    u'SkyElevator.pythonanywhere.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## 3rd party apps
    'crispy_forms',
    'rest_framework',

    ## own apps
    'accounts.apps.AccountsConfig',
    'documents.apps.DocumentsConfig',
    'projects.apps.ProjectsConfig',

]

## install with pip install django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SEBE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, '_static/html'),
            os.path.join(BASE_DIR, 'accounts/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                ## to use {{ MEDIA_URL }} in templates
                'django.template.context_processors.media', 
            ],
        },
    },
]

WSGI_APPLICATION = 'SEBE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Colombo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '_static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, '_static_root') ## python3 manage.py collectstatic

## media files will be stored as MEDIA_ROOT/[public, private]/<app_name>/<model_name>/<file_name>
MEDIA_DIR_NAME = '_media'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_DIR_NAME)
MEDIA_ROOT_PRIVATE = os.path.join(BASE_DIR, MEDIA_DIR_NAME, 'private')
MEDIA_ROOT_PUBLIC = os.path.join(BASE_DIR, MEDIA_DIR_NAME, 'public')

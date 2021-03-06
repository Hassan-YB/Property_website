"""
Django settings for helloworld project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o%i%*isj33dp$xp4hef(cra%_s0rq--#m%)qxi8g3acp)9-ntn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'allauth', 
    'allauth.account', 
    #First for allauth
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google', 
    'allauth.socialaccount.providers.facebook', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sailor',
]
SITE_ID = 1

MIDDLEWARE = [
    #First 2 for sessions in allauth
    
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helloworld.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #below 2 for allauth directory
        'DIRS': [os.path.join(BASE_DIR,'sailor', 'templates','allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request', 
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = ( 
	'django.contrib.auth.backends.ModelBackend', 
	'allauth.account.auth_backends.AuthenticationBackend', 
)


WSGI_APPLICATION = 'helloworld.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'booking',
        'USER': 'root',
        'PASSWORD': 'Helloworld123',
        'HOST':'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT  =   os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sailor','static'),]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

#Allauth login redirect to homepage
LOGIN_REDIRECT_URL = '/'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hassanbaras5@gmail.com'
EMAIL_HOST_PASSWORD = 'Wondermay2795'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
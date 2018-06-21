# -*- coding: utf-8 -*
"""
Django settings for metamap_django project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from init_config import result

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nyps=8t#p69#1a$be^m^)c$_3k^*7aldic%p(8jnzh=@wcbk1w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = result.get('DEBUG', False)

START_PORT = 10000
END_PORT = 60000
MARATHON_HOST = result['MARATHON_HOST']
PROMETHEUS_HOST = result['PROMETHEUS_HOST']
PROMETHEUS_HOME = result.get('PROMETHEUS_HOME', '/server/share/prometheus/')

SESSION_COOKIE_NAME = 'runningdata_sid'
CSRF_COOKIE_NAME = 'runningdata_csrftoken'
ALLOWED_HOSTS = result.get('ALLOWED_HOSTS',
                           ['127.0.0.1', '10.2.19.62',
                            '10.1.5.83', '10.2.19.124', '10.103.27.171', '10.103.70.27'])

# 设置cas服务器地址
CAS_SERVER_URL = "http://{server_name}/sso/".format(server_name=result['CAS_SERVER_URL'])
CAS_IDC_SERVER_URL = result.get("CAS_IDC_SERVER_URL", "http://10.2.19.113:8181/sso/")
# CAS_LOGOUT_COMPLETELY = True
CAS_PROVIDE_URL_TO_LOGOUT = True
# CAS_GATEWAY = True

# push url
PUSH_URL = result['PUSH_URL']
PUSH_KEY = result['PUSH_KEY']
ADMIN_PHONE = 'PWy9rKUlzFLGO8Ry6v368w=='
ADMIN_EMAIL = result['ADMIN_EMAIL']

# email settings
EMAIL_HOST = result['EMAIL_HOST']
EMAIL_HOST_USER = result['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = result['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = result.get('EMAIL_USE_TLS', False)
EMAIL_PORT = result.get('EMAIL_PORT', 465)
EMAIL_USE_SSL = result.get('EMAIL_USE_SSL', True)

from celery_conf import *

# Application definition
INSTALLED_APPS = [
    'will_common',
    'running_alert',
    'cas',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE_CLASSES = [
    'will_common.middleware.viewexception.ViewException',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'will_common.middleware.viewexception.LoginRequire',
    'cas.middleware.CASMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'will_common.middleware.accesstracer.AccessTracer',
]

ROOT_URLCONF = 'metamap_django.alert_urls'

### Add authentication backends for cas

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'metamap_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': result['MAIN_DB_NAME'],
        'PASSWORD': result['MAIN_DB_PWD'],
        'USER': result['MAIN_DB_USER'],
        'HOST': result['MAIN_DB_HOST'],
        'PORT': result['MAIN_DB_PORT'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = "/usr/local/metamap/static"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
        # 日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': result['ALL_LOG'],  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': result['ERROR_LOG'],
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/running_alert_script.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'marathon': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'running_alert': {
            'handlers': ['default', 'console', 'error_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

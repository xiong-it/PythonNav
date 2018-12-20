"""
Django settings for sso project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3gz*#-yscbp=h)g!ck^hh9lf@kxg!flm6l3f@5^c$ki%w*c=x4'

# SECURITY WARNING: don't run with debug turned on in production!
database_user = 'root'
database_pwd = ''


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'sso_server',
    'crispy_forms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sso.urls'

WSGI_APPLICATION = 'sso.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portal',
        'USER':database_user,
        'PASSWORD':database_pwd,
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# STATIC_ROOT = 'static/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static').replace('\\', '/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
LOGIN_REDIRECT_URL = '/'

LOG_ROOT = BASE_DIR + '/logs/'
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'INFO': {
            '()': 'log.LevelFilter',
            'name': 'INFO',
        },
        'WARNING': {
            '()': 'log.LevelFilter',
            'name': 'WARNING',
        },
        'ERROR': {
            '()': 'log.LevelFilter',
            'name': 'ERROR',
        },
        'DEBUG': {
            '()': 'log.LevelFilter',
            'name': 'DEBUG',
        }
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + '/debug.log',
            'formatter': 'verbose',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + '/info.log',
            'formatter': 'verbose',
            'filters': ['INFO'],
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + '/error.log',
            'formatter': 'verbose',
            'filters': ['ERROR'],
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + '/warning.log',
            'formatter': 'verbose',
            'filters': ['WARNING'],
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['info', 'error', 'debug'],
            'level': 'DEBUG',
            'propagate': True,
            'formatter': 'verbose',
        },
        'sso_server': {
            'handlers': ['info', 'error', 'debug', 'warning'],
            'propagate': True,
            'level': 'INFO',
            'formatter': 'verbose',
        },
    },
}

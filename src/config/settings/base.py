from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv


# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(dotenv_path=BASE_DIR / '.env')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED', 'http://127.0.0.1').split(',')


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Apps
    'apps.core.apps.CoreConfig',
    'apps.public.apps.PublicConfig',
    'apps.account.apps.AccountConfig',
    'apps.customers.apps.CustomersConfig',
    'apps.subscription.apps.SubscriptionConfig',
    'apps.payment.apps.PaymentConfig',
    'apps.notification.apps.NotificationConfig',
    'apps.course.apps.CourseConfig',
    'apps.ticket.apps.TicketConfig',

    # Django modules
    'tinymce',
    'django_q',
    'azbankgateways',
    'django_cleanup.apps.CleanupConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGES = [
    ('fa', _("Persian")),
]

LOCALE_PATHS = [
    BASE_DIR / os.getenv('LOCALE_PATHS', 'locale'),
    os.getenv('DJANGO_Q_LOCALE_PATH', BASE_DIR / 'locale/django_q'),
    os.getenv('IRANIAN_BANK_GATEWAY_LOCALE', BASE_DIR / 'locale/az_bank_locale')
]

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = False

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_ROOT', BASE_DIR / 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / os.getenv('STATICFILES_DIRS', 'static/assets/'),
]

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / os.getenv('MEDIA_ROOT', 'static/media')

# Production whitenoise
if int(os.getenv('ENABLE_WHITENOISE', default=0)):
    # Insert Whitenoise Middleware and set as StaticFileStorage
    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'


# Auth user model
AUTH_USER_MODEL = 'account.User'


# Redis db config
REDIS_CONFIG = {
    'active': int(os.getenv('REDIS_ACTIVE', 0)),  # 1 redis is connected, 0 not connected
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': int(os.getenv('REDIS_PORT', 6379))
}

# SMS config
SMS_CONFIG = {
    'API_KEY': os.getenv('SMS_CONFIG_API_KEY'),
    'ORIGINATOR': os.getenv('SMS_CONFIG_ORIGINATOR')
}


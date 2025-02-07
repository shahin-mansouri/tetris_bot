"""
Django settings for tetris_bot project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
# yV6uzymfb95#_ZKP
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)e+xw&vh9h6=_=$av@q1!)l0co#o8ij%b7n8n^g)5y5lavol#&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok-free.app']
# ALLOWED_HOSTS = ['46.249.99.31', 'localhost', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://*.ngrok-free.app']
# Application definition

INSTALLED_APPS = [
    'youtube_auth.apps.YoutubeAuthConfig',
    'x_auth.apps.XAuthConfig',
    'notifications.apps.NotificationsConfig',
    'awards.apps.AwardsConfig',
    'verify_token.apps.VerifyTokenConfig',
    'invition.apps.InvitionConfig',
    'telegram_bot.apps.TelegramBotConfig',
    'accounts.apps.AccountsConfig',
    'home.apps.HomeConfig',
    'tetris.apps.TetrisConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'tetris_bot.urls'

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

WSGI_APPLICATION = 'tetris_bot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'telegram_bot': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'new_airdrop_db',
        'USER': 'new_airdrop_user',
        'PASSWORD': 'new_airdrop_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
DATABASE_ROUTERS = ['tetris_bot.db_router.TelegramBotRouter']



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'accounts.TelegramUser'
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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # مسیر به دایرکتوری استاتیک
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


import os

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 


# تنظیمات توییتر
# bearer token: AAAAAAAAAAAAAAAAAAAAAGnIyQEAAAAAC3aRjjglfqr9cqtTiyy0ImtCBTw%3DMczvbvE26TJU7mpmkLB1FAl1Yv1yrV08Ea6x9ymGj8kdhhtu7d
API_KEY = 'qmIDbwXzADLKbjme5e2g2VFHk'
API_SECRET_KEY = 'kKjH0XF5UwJtcYhGuGw56effKgfgwvSlCsckJsGXhhI2L9pRK6'
ACCESS_TOKEN = '1881635679135780864-n8KWymi5XGwdqbgVmNdtCCWDIwxqYU'
ACCESS_TOKEN_SECRET = '1ueAu6pr23R2WAfA55OUy4WakHLcwzBdibPidAx9Jded5'
# CALLBACK_URI = 'http://127.0.0.1:8000/x-auth/callback/'  # مسیر بازگشت
TWITTER_CALLBACK_URI = 'https://4f7a-149-36-50-236.ngrok-free.app/x-auth/callback/'  # مسیر بازگشت
TWITTER_CLIENT_ID = 'WWV2QjhXbEU0OTExeXRONTR3SHU6MTpjaQ'
TWITTER_CLIENT_SECRET = 'EX4RtItJx8q7bGHm1Yg1rlF5JANDvl9ijEpZSdmDFuii8rIJwn'
TWITTER_HANDLE = 'ShahinManso'
TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAGnIyQEAAAAAC3aRjjglfqr9cqtTiyy0ImtCBTw%3DMczvbvE26TJU7mpmkLB1FAl1Yv1yrV08Ea6x9ymGj8kdhhtu7d'

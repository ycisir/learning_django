"""
Django settings for learning_django project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# my changes **********************
# TEMPLATE_DIR = BASE_DIR / 'templates'
# STATIC_DIR = BASE_DIR / 'static'
# my changes **********************

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yvx&%5@(3rbtfwhyhva^z22q@^=*zeoud=^cy5^##54vqf!=ry'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# my changes **********************

EXTERNAL_APPS = [
    'core',
    'course',
    'fees',
    'enroll',
    'student',
    'blog',
    # 'blog.apps.BlogConfig'
    'school',
]

INSTALLED_APPS += EXTERNAL_APPS

# my changes **********************

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ======================= cache ===================
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # ======================= cache end ===================
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # =============== my middleware ==========================
    # 'blog.middlewares.MyProcessMiddleware',
    # 'blog.middlewares.MyExceptionMiddleware',
    'blog.middlewares.MyTemplateResponseMiddleware',
    


]

ROOT_URLCONF = 'learning_django.urls'

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

WSGI_APPLICATION = 'learning_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "learn_db",
        "USER": "yasir",
        "PASSWORD": "1912",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# my changes **********************
# STATICFILES_DIRS = [STATIC_DIR]
# print(STATICFILES_DIRS)
# my changes **********************

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# ========================================= our code ========================
# important
# SESSION_COOKIE_AGE = 10
# SESSION_COOKIE_NAME = 'sessionname'
# SESSION_COOKIE_PATH = '/home'



# not important
# SESSION_COOKIE_HTTPONLY = True by default set true
# SESSION_COOKIE_SECURE = True
# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_FILE_PATH = BASE_DIR / 'session'
# SESSION_COOKIE_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SAVE_EVERY_REQUEST = False

# CACHE_MIDDLEWARE_SECONDS = 30

# database caching===========================================
CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'core_cache',
    }
}

# filebase caching===========================================
# suitable
# CACHES = {
#     'default': {
#         'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION':'/home/yasir/Documents/projects/django/learning_django/cache',
#     }
# }

# localmemory caching===========================================
# dont use in production
# CACHES = {
#     'default': {
#         'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION':'unique-snowflake',
#     }
# }
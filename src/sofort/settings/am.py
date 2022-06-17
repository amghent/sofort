"""
Django settings for sofort project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-byo_((p0+icxcocxnn(-$8vcef!8v5p=e72!@6^0y^1y-%q97q'

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

    'bootstrap.apps.BootstrapConfig',
    'core.apps.CoreConfig',

    'bookmarks.apps.BookmarksConfig',
    'forums.apps.ForumsConfig',
    'interests.apps.InterestsConfig',
    'issues.apps.IssuesConfig',
    'links.apps.LinksConfig',
    'members.apps.MembersConfig',
    'newsletters.apps.NewslettersConfig',
    'pages.apps.PagesConfig',
    'questions.apps.QuestionsConfig',
    'tags.apps.TagsConfig',
    'tutorials.apps.TutorialsConfig'
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

ROOT_URLCONF = 'sofort.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, '..', '_templates', 'default'),
            os.path.join(BASE_DIR, '..', 'core', 'templates'),
            os.path.join(BASE_DIR, '..', 'interests', 'templates'),
            os.path.join(BASE_DIR, '..', 'pages', 'templates'),
            os.path.join(BASE_DIR, '..', 'questions', 'templates')
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'environment': 'sofort.jinja2.environment'
        },
    },

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

WSGI_APPLICATION = 'sofort.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

###
# sidviny - 2022-06-15
# This database will go in /db.  Make sure it exists.
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', '..', 'db', 'db.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'nl-be'
TIME_ZONE = 'Europe/Brussels'
USE_I18N = True
USE_TZ = True
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', '_templates', 'default', 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

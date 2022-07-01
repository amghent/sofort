import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'grappelli',
    'filebrowser',
    
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
            os.path.join(BASE_DIR.parent, '_templates', 'default'),
            os.path.join(BASE_DIR.parent, 'core', 'templates'),
            os.path.join(BASE_DIR.parent, 'interests', 'templates'),
            os.path.join(BASE_DIR.parent, 'pages', 'templates'),
            os.path.join(BASE_DIR.parent, 'questions', 'templates')
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

LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'Europe/Brussels'
USE_I18N = True
USE_TZ = True
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M'

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, '_templates', 'default', 'static'),
]

TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/js/tinymce/tinymce.min.js")
TINYMCE_COMPRESSOR = False

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR.parent.parent, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# TODO: Autofield can be used maybe to generate a simple ID for a question,
# which is more readable than the UUID in the URL

LOGIN_URL = 'index'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

from sofort.settings.common import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sofort-dev',
        'USER': 'sofort',
        'PASSWORD': 'sofort',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

DEBUG = True

SECRET_KEY = 'django-insecure-byo_((p0+icxcocxnn(-$8vcef!8v5p=e72!@6^0y^1y-%q97q'

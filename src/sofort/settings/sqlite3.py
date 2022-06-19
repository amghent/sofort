from sofort.settings.common import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR.parent.parent, 'db', 'db.sqlite3'),
    },
}

DEBUG = True

SECRET_KEY = 'django-insecure-byo_((p0+icxcocxnn(-$8vcef!8v5p=e72!@6^0y^1y-%q97q'

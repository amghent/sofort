from sofort.settings.common import *

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "sofort",
        "USER": "sofort",
        "PASSWORD": "Sofort_pwd",
        "HOST": "localhost",
        "PORT": "1433",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server"},
    },
}

DEBUG = True

SECRET_KEY = 'django-insecure-byo_((p0+icxcocxnn(-$8vcef!8v5p=e72!@6^0y^1y-%q97q'

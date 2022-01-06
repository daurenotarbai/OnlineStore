import os
LANGUAGE_CODE = 'ru-ru'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')b_1$a+85=l2(6=ucdp!r58$z1#9_pzg6yed=za)5i!%)k)2^tdauren'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1","0.0.0.0'"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onlinestore',
        'USER': 'dauren',
        'PASSWORD': 'sungat97',
        'HOST':'localhost',
        'PORT':'5432',

    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

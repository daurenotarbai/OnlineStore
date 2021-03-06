import os
LANGUAGE_CODE = 'ru-ru'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = ')b_1$a+85=l2(6=ucdp!r58$z1#9_pzg6yed=za)5i!%)k)2^t'

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST':'onlinestore_db',
        'PORT':'5432',

    }
}




STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]

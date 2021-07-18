import os
from .db import DATABASES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'django-insecure-)d25%ehh^03n9$(qcq3gp$c$i27o0@k2%f#61v401f^c@mwa66'

DEBUG = False

ALLOWED_HOSTS = ['192.168.1.107']

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': '4412270865460649',
            'secret': 'e2514b1cae74f08a90fa52bddbb33e0d',
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ADMIN_EMAIL = 'oleksandrboliukh@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'oleksandrboliukh@gmail.com'
EMAIL_HOST_PASSWORD = '%0504Cfyz'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

PORTAL_URL = 'http://localhost:8000'

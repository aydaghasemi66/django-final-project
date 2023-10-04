from config.settings import*

SECRET_KEY = 'django-insecure-d%vqk$_l=t$ujs3ga-i0wd44@t$yj^_#0+)wrkvildk15#lr_c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT=BASE_DIR/'/static'
MEDIA_ROOT=BASE_DIR/'media'
STATICFILES_DIRS=[
    BASE_DIR/'static',
    BASE_DIR/'media',
]

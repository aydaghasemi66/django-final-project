from config.settings import*

SECRET_KEY = 'django-insecure-d%vqk$_l=t$ujs3ga-i0wd44@t$yj^_#0+)wrkvildk15#lr_c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['djangoresume.ir','www.djangoresume.ir']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='mail.djangoresume.ir'
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER='admin@djangoresume.ir'
EMAIL_HOST_PASSWORD='TNi5XJS4Ygru44u'
DEFAULT_FROM_EMAIL='admin@djangoresume.ir'

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE='Strict'
SESSION_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
X_FRAME_OPTION='DENY'
SECURE_HSTS_SECONDS=15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
CSP_DEFAULT_SRC=("'none'")
CSP_STYLE_SRC=("'self'")
CSP_SCRIPT_SRC=("'self'")
CSP_FONT_SRC=("'self'")
CSP_IMG_SRC=("'self'")

import os

import environ

root = environ.Path(__file__) - 2  # get root of the project
env = environ.Env()
environ.Env.read_env(root('.env'))

BASE_DIR = root()
SITE_ROOT = root()

DEBUG = env.bool('DEBUG', default=False)
FLATPAGES = env.bool('FLATPAGES', default=False)
ALLOWED_HOSTS = ['*']
SECRET_KEY = env.str('SECRET_KEY')
JWT_ENABLE = env.bool('JWT_ENABLE', default=False)

DATABASES = {'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')}
MEDIA_ROOT = root('media')
MEDIA_URL = env.str('MEDIA_URL', default='/media/')
STATIC_ROOT = root('static')
STATIC_URL = env.str('STATIC_URL', default='/static/')
TEMPLATES_DIR = 'templates'

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = 'index'

ROOT_URLCONF = 'govparser.urls'
WSGI_APPLICATION = 'govparser.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

# AUTH_USER_MODEL = 'django.contrib.admin.User'
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

if JWT_ENABLE:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].insert(
        0, 'rest_framework_simplejwt.authentication.JWTAuthentication'
    )

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ["127.0.0.1"]
    CACHES = {'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

if FLATPAGES:
    INSTALLED_APPS.append('django.contrib.sites')
    INSTALLED_APPS.append('django.contrib.flatpages')
    SITE_ID = 1

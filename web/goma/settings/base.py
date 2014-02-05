import os.path as path

BASE_DIR = path.dirname(path.dirname(path.dirname((__file__))))

SECRET_KEY = '4gzx8fyhzsv(eqlnn@*9epm2*qyr96_q+f5-fnt*-as$ol38cu'

ALLOWED_HOSTS = []


APPEND_SLASH = False
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_bcrypt',
    'south',
    'rest_framework',

    'accounts',
    'teachers',
    'students',
    'klasses',
    'schools',
    'parents',
    'notes',
    'leads',
    'supers',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'goma.urls'

WSGI_APPLICATION = 'goma.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

STATIC_ROOT = path.join(BASE_DIR, 'public', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path.join(BASE_DIR, 'static'),
)
PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
    'react.utils.pipeline.JSXCompiler',
)

TEMPLATE_DIRS = (
    path.join(BASE_DIR, 'templates'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gomadb',
        'USER': 'goma',
    }
}

AUTH_USER_MODEL = 'accounts.User'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
)

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


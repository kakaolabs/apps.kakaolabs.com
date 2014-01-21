import os
import sys
import dj_database_url
sys.path.append(os.getcwd())

from ConfigParser import RawConfigParser
from ConfigParser import NoOptionError

config = RawConfigParser()
host_type = os.getenv('HOST_TYPE')
if host_type == 'PRODUCTION':
    config_filepath = 'kakaolabs/config/production.ini'
elif host_type == 'STAGING':
    config_filepath = 'kakaolabs/config/staging.ini'
elif host_type == 'LOCALHOST':
    config_filepath = 'kakaolabs/config/localhost.ini'
config.read(config_filepath)

def get_config(name, default=None):
    try:
        return config.get('config', name)
    except NoOptionError, e:
        return os.environ.get(name, default)


# django config
PROJECT_ROOT = os.path.dirname(__file__)
ROOT_URLCONF = 'core.urls'
AUTH_USER_MODEL = 'core.Member'
WSGI_APPLICATION = 'core.wsgi.application'

# domain
DOMAIN = get_config('DOMAIN', 'http://kakaolabs.com')
TEMPLATE_DEBUG = DEBUG = get_config('DEBUG', False)
MANAGERS = ADMINS = ()
ALLOWED_HOSTS = ['*']

# database
DATABASES = {
    'default': dj_database_url.config()
}

if os.getenv('LOADDATA'):
    DATABASES['default']['OPTIONS'] = {'init_command': 'SET FOREIGN_KEY_CHECKS = 0;'}

SOUTH_TESTS_MIGRATE = False


# timezone and language
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True

# directories
TEMP_DIR = '/tmp/'
MEDIA_ROOT = ''
STATIC_ROOT = ''
MEDIA_URL = get_config('MEDIA_URL')
STATIC_URL = get_config('STATIC_URL')

# static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = get_config('SECRET_KEY')

# templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
)

# middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 # 30 days


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',

    # 3rd party apps
    'south',  # for migrations

    # kakaolabs apps
    'core',
    'sms',
)


# testing
if DEBUG:
    INSTALLED_APPS += ('django_nose', )
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
    }
}

if get_config('SIMPLEPRINTS_DEBUG_SQL'):
    LOG_ROOT = 'log/'
    LOGGING['loggers'].update({
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
    })


# authenticate
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
 )
AUTH_PROFILE_MODULE = 'core.Member'
LOGIN_REDIRECT_URL = '/'

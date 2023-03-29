from datetime import timedelta
from pathlib import Path
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_path = BASE_DIR / ".env"
if env_path.is_file():
    environ.Env.read_env(env_file=str(env_path))


SECRET_KEY = env("SECRET_KEY", default="ewfi83f2ofee3398fh2ofno24f")

DEBUG = env("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=list, default=["*"])


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photos.apps.PhotosConfig',
]

MIDDLEWARE = [
    'django_aws.middleware.health_check_middleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_aws.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_aws.wsgi.application'

DATABASES = {
    'default': env.db(default="postgresql://postgres:postgres@127.0.0.1:5432/django_aws")
}



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


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="sqs://localhost:9324")
CELERY_TASK_DEFAULT_QUEUE = env("CELERY_TASK_DEFAULT_QUEUE", default="default")
CELERY_BEAT_SCHEDULE = {
    "beat_task": {
        "task": "django_aws.tasks.beat_task",
        "schedule": timedelta(seconds=5),
    },
}
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "region": env("AWS_REGION", default="us-east-1")
}

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="")

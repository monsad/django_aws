import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_path = BASE_DIR / ".env"
if env_path.is_file():
    environ.Env.read_env(env_file=str(env_path))


DATABASES = {
    'default': env.db(default="postgresql://postgres:postgres@127.0.0.1:5433/django_aws")
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]



STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"

DEBUG = True

ALLOWED_HOSTS = ['*']
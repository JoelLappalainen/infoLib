
from infoLib.settings.base import *
import os

# Parse database configuration from $DATABASE_URL
import dj_database_url

# # Allow all host hosts/domain names for this site
ALLOWED_HOSTS = ['*']

DATABASE_URL = ['DATABASE_URL']

DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# we only need the engine name, as heroku takes care of the rest
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

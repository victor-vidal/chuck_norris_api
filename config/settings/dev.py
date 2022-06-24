from .base import *

DEBUG = True

ALLOWED_HOSTS.append('*')

CORS_ORIGIN_ALLOW_ALL = True

DATA_UPLOAD_MAX_MEMORY_SIZE = None

CURRENT_ENV = os.environ.get('CURRENT_ENV')
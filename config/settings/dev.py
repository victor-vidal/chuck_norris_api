import os

from .base import *

DEBUG = True

ALLOWED_HOSTS.append('*')

CORS_ORIGIN_ALLOW_ALL = True

DATA_UPLOAD_MAX_MEMORY_SIZE = None

CURRENT_ENV = os.environ.get('CURRENT_ENV')

# ================================ rabbitmq ====================================
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True
CELERY_ACKS_LATE = False
CELERY_TASK_ALWAYS_EAGER = False

RABBIT_HOSTNAME = os.environ.get('RABBIT_HOSTNAME')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', '')
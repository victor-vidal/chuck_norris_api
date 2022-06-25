import os

from celery import Celery
from kombu import Queue, Exchange

current_env = os.environ.get('CURRENT_ENV')

app = Celery('chuck-norris-api')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# This command sets Django settings as a configuration source for Celery.
app.config_from_object('django.conf:settings', namespace='CELERY')

default_exchange = Exchange('chuck_norris_api')

app.conf.task_queues = (
    Queue(
        f'subscription_random_category_joke_{current_env}',
        default_exchange,
        routing_key='subscription_random_category_joke',
        queue_arguments={'x-max-priority': 15}
    ),
)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

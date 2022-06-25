from celery.schedules import crontab

from config.celery import app, current_env

from jokes.services import SubscriptionDeliveryService

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        send_random_category_joke_to_subscriber_async.s(),
        name='subscription_random_category_joke_sender'
    )
    
@app.task(queue=f'subscription_random_category_joke_{current_env}')
def send_random_category_joke_to_subscriber_async():
    subscription_delivery_service = SubscriptionDeliveryService()
    subscription_delivery_service.execute()
    return True
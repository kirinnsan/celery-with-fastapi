import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_BACKEND_URL", "redis://localhost:6379")


@celery.task(name="create_task")
def create_task(wait_time: int):
    time.sleep(wait_time * 10)
    return True

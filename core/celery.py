from __future__ import absolute_import , unicode_literals
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery("core", broker=os.environ.get("CLOUD_AMPQ_URL"))

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
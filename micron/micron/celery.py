import os
from celery import Celery



# install the standard Django settings module
# for the Celery program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'micron.settings')
app = Celery('micron')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
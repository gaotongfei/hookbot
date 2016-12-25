import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hookbot.settings.development')

app = Celery('hookbot')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

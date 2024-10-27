from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configura la variable de entorno DJANGO_SETTINGS_MODULE para que apunte a settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orders_project.settings')

# Crear una instancia de Celery
app = Celery('orders_project')

# Configura Celery para que use las configuraciones del archivo settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente las tareas en las aplicaciones registradas en INSTALLED_APPS
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

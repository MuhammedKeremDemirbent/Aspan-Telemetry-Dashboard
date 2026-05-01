import os
from celery import Celery

# Django ayarlarına ulaşabilmek için environment variable set ediyoruz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Django ayarlarını Celery için paylaşıyoruz (CELERY_ ile başlayanları okur)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Uygulamalardaki asenkron görevleri (tasks.py) otomatik bulur
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

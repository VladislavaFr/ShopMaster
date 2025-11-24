import os
from django.core.wsgi import get_wsgi_application

# Указываем путь к настройкам
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаем объект приложения WSGI
application = get_wsgi_application()

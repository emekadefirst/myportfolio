# from whitenoise import WhiteNoise

# application = WhiteNoise(application, root="staticfiles")
# application.add_files("staticfiles", prefix="more-files/")

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

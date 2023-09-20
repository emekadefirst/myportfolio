from whitenoise import WhiteNoise
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Create the Django application
application = get_wsgi_application()

# Configure WhiteNoise to serve static files
application = WhiteNoise(application, root="staticfiles")
application.add_files("staticfiles", prefix="more-files/")

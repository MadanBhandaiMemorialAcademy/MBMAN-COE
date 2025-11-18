import os
import sys

# Path to your project root
project_home = '/home/mbmanedu/mbcoe.mbman.edu.np'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

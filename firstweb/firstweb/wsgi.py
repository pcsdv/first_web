"""
WSGI config for secondweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstweb.settings')
# for multiple django sites
os.environ['DJANGO_SETTINGS_MODULE']= "firstweb.settings"

application = get_wsgi_application()


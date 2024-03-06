"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddleware
from . import routing
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":AuthMiddleware(URLRouter(
        routing.websocket_urlpatterns
    ))
})

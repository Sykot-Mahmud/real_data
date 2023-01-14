"""
ASGI config for realtime project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from core.routing import ws_urlpatterns



"""
When the ASGI server loads your application, Django needs to import the settings module — that’s 
where your entire application is defined.

Django uses the DJANGO_SETTINGS_MODULE environment variable to locate the appropriate settings module.

"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime.settings')


"""
Protocol type router that determines the next routing handler based on its transport protocol. 
Hence you can define a router for HTTP and another for WebSocket messages.
"""
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})

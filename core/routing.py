from django.urls import path
from .consumers import WSConsumer



"""
While consumers are valid ASGI applications, 
you don’t want to just write one and have that be the only thing you can give to protocol serverslike Daphne.
Channels provides routing classes that allow you to combine and stack your consumers 
(and any other valid ASGI application) to dispatch based on what the connection is.
"""
ws_urlpatterns=[
    path('ws/some_url/',WSConsumer.as_asgi())
]
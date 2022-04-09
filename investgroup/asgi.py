"""
ASGI config for realtime project.

it  exposes the ASGI callable as a module-level variable named ''application''.

For more information on this file, see
https://docsdjangoproject.com/en/3.1/howto/deployment/asgi/

"""
from channels.auth import AuthMiddlewareStack, URLRouter
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from crypto.routing import ws_urlpatterns
import os


os.environ.setdefault('DAJNGO_SETTINGS_MODULE','investgroup.settings')

application = ProtocolTypeRouter({ 

    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(crypto.routing.ws_urlpatterns))

})

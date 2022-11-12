"""
ASGI config for async_web project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_web.settings') 

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({ # This is the ASGI entrypoint. ProtocolTypeRouter is a router that allows you to route different protocols to different application instances. It takes a dictionary of protocol names to application instances. 
	"http": get_asgi_application(), # The http protocol maps to the Django ASGI application.
	"websocket": AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns)), # The websocket protocol maps to the ChatConsumer.
})

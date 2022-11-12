from django.urls import re_path # re_path is the same as path, but it accepts regular expressions

from .consumer import ChatConsumer

websocket_urlpatterns = [ # websocket_urlpatterns is a list of URL patterns that will be passed to Django's URL router. 
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()), # as_asgi() is a method that converts a consumer class into an ASGI application.
]
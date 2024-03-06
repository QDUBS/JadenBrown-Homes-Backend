from django.urls import re_path
from chat.consumer import ChatConsumer


websocket_urlpatterns = [
    re_path(r"chat", ChatConsumer.as_asgi())
]
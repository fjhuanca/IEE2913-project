from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from esp_comm import consumer

websocket_urlPatter = [
    path('ws/polData/', consumer.DashConsumer.as_asgi()),
]
application = ProtocolTypeRouter({
    'websocket' :AuthMiddlewareStack(URLRouter(websocket_urlPatter))
    
})
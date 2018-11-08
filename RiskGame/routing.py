from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from .consumer import GameConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator( #Allowing only trusted origins to connect
        AuthMiddlewareStack(
            URLRouter([
                path('play', GameConsumer)
            ])
        )
    )
})

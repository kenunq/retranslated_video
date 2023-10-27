import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "retranslated_screen.settings")

qq = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

from main import routing

print(routing.websocket_urlpatterns)

application = ProtocolTypeRouter({
    'http': qq,
    'websocket':
        AllowedHostsOriginValidator(AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    )
})

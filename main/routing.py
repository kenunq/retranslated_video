from django.urls import re_path
from main import consumers

print(consumers.ScreenShareConsumer)

websocket_urlpatterns = [
    re_path('ws/myscreen/', consumers.ScreenShareConsumer.as_asgi()),
]
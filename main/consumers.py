import asyncio
import json

import pyautogui as pyautogui
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.layers import get_channel_layer
import cv2
import base64
import numpy as np


class ScreenShareConsumer(WebsocketConsumer):
    def __init__(self):
        super().__init__()
        print("123")
    def connect(self):
        print("123")
        self.room_group_name = "send_video"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()
        print('connect')

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
        print('disconnect')

    def receive(self, text_data):
        # Обработка сообщений, если необходимо
        pass

    def send_video_stream(self, event):
        # while True:
        #     # Захват кадра с экрана (здесь нужно добавить код захвата)
        #     img = pyautogui.screenshot()
        #     frame = np.array(img)
        #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #
        #     # Преобразование кадра в строку base64
        #     _, buffer = cv2.imencode('.jpg', frame)
        #     jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        #
        #     # Отправка кадра клиенту
        #     self.send(text_data=json.dumps({'frame': jpg_as_text}))
        self.send(text_data=json.dumps({'frame': "jpg_as_text"}))
        print('send_video_stream')

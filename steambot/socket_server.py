from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json



class SocketServer(WebsocketConsumer):
    def connect(self):
        accept = False

        if self.scope['path'] == '/ws/bot/':
            accept = True
            async_to_sync(self.channel_layer.group_add)("bot", self.channel_name)
            print(async_to_sync)

        if accept:
            print(accept)
            self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("bot", self.channel_name)

    # Receive message from room group
    def chat_message(self, event):

        self.send(text_data=event["text"])

        
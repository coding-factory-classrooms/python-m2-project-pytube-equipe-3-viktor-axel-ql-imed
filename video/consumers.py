import json
from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("connection")
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(type(text_data_json))
        message = text_data_json["message"]

        self.send(text_data=json.dumps({
            'message': message
        }))

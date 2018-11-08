from channels.generic.websocket import WebsocketConsumer
import json
from . import controller

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send("Test message sent from Server")

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        #message = text_data_json['message']
        #Do Calculations
        #self.send(text_data=json.dumps({}))

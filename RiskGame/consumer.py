from channels.generic.websocket import WebsocketConsumer
import json
from . import controller

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(json.dumps({
            type: "initialization",
            armies: controller.game.getIds()
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        controller.handleRecieved(text_data)
        #self.send(text_data=json.dumps({}))

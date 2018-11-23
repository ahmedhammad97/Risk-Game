from channels.generic.websocket import WebsocketConsumer
import json
from . import controller

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Wohooo .. Connected to client!")
        self.send(controller.renderMap())
        controller.startTurn()

    def disconnect(self, close_code):
        print("WebSocket connection is lost...")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        #controller.handleRecieved(text_data)
        print(text_data_json["message"])
        #self.send(text_data=json.dumps({}))

    def sendWinnerMessage(self, message):
        toSend = {
            "type" : "winning",
            "message" : message
        }
        self.send(json.dumps(toSend))

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
        controller.handleRecieved(text_data)

    def sendWinnerMessage(self, message, winner):
        toSend = {
            "type" : "winning",
            "message" : message,
            "winner" : winner
        }
        self.send(json.dumps(toSend))

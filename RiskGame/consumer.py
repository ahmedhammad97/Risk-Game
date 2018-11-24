from channels.generic.websocket import WebsocketConsumer
import json
from . import controller

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Wohooo .. Connected to client!")
        self.render()
        self.startTurn()

    def render(self, type="render", message=None):
        self.send(controller.renderMap(type, message))

    def startTurn(self):
        toSendData = controller.startTurn()
        self.send(toSendData)

    def disconnect(self, close_code):
        print("WebSocket connection is lost...")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.handleRecieved(text_data_json)

    def handleRecieved(self, data):
        if data["type"] == "deploymentSuccess":
            toSendData = controller.completeTurn()
            self.send(toSendData)
        elif data["type"] == "attackSuccess":
            endTurnData = controller.endturn()
            if endTurnData["flag"]:
                self.sendWinnerMessage(endTurnData["winner"])
            else:
                self.startTurn()
        elif data["type"] == "deployResponse":
            #Update Map
            #Continue normal deployRender
            pass
        elif data["type"] == "attackResponse":
            #Update Map
            #Continue normal attackRender
            pass

    def requestDeploy(self):
        self.send(json.dumps({"type" : "deployInputRequest"}))

    def requestAttack(self):
        self.send(json.dumps({"type" : "attackInputRequest"}))

    def sendWinnerMessage(self, winner):
        message = winner + " player won the game .. Wohooo!"
        toSend = {
            "type" : "winning",
            "message" : message,
            "winner" : winner
        }
        self.send(json.dumps(toSend))

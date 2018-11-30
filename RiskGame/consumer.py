from channels.generic.websocket import WebsocketConsumer
import json
from . import controller

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("Wohooo .. Connected to client!")
        self.render() #Send initial random map
        self.startTurn() #First turn call

    def render(self, type="render", message=None):
        self.send(controller.renderMap(type, message))

    def startTurn(self):
        toSendData = controller.startTurn()
        if toSendData == "HumanDeploy":
            self.requestDeploy(controller.getBonus(), controller.getColor())
        else:
            self.send(toSendData)

    def disconnect(self, close_code):
        print("WebSocket connection is lost...")

    def receive(self, text_data):
        text_data_json = json.loads(text_data) #Parse Json object to Python-like object
        self.handleRecieved(text_data_json)

    def handleRecieved(self, data):
        if data["type"] == "error":
            endTurnData = controller.endturn()
            if endTurnData["flag"]:
                self.sendWinnerMessage(endTurnData["winner"])
            else:
                self.startTurn()
        elif data["type"] == "deploymentSuccess": #Human agent deployment request
            toSendData = controller.completeTurn()
            self.send(toSendData)
        elif data["type"] == "attackSuccess": #Human agent attack request
            endTurnData = controller.endturn()
            if endTurnData["flag"]:
                self.sendWinnerMessage(endTurnData["winner"])
            else:
                self.startTurn()
        elif data["type"] == "deployResponse": #Human agent deployment response
            #Update Map
            controller.updateMapByHuman(data)
            #Continue normally
            self.requestAttack()

        elif data["type"] == "attackResponse": #Human agent attack request
            #Update Map
            controller.updateMapByHuman(data)
            #Continue normal attackRender
            endTurnData = controller.endturn()
            if endTurnData["flag"]:
                self.sendWinnerMessage(endTurnData["winner"])
            else:
                self.startTurn()

    def requestDeploy(self, armies, color):
        toSend = {"type" : "deployInputRequest"}
        toSend["armies"] = armies
        toSend["color"] = color
        self.send(json.dumps(toSend))

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

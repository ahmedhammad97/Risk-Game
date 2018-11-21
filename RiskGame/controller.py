from .model import Game
import json

game = None

def prepare(data):
    global game
    game = Game.Game(data["map"], data["playerOne"], data["playerTwo"])

def initialize():
    global game
    items = game.toRender()
    result =  {"type": "render", "nodes": []}
    for item in items:
        result["nodes"].append(item)
    return json.dumps(result)

def handleRecieved(message):
    pass

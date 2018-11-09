from .model import Game
import json

game = None

def prepare(data):
    global game
    game = Game.Game(data["map"], data["playerOne"], data["playerTwo"])

def initialize():
    global game
    return json.dumps({
        "type": "initialization",
        "nodes": game.toRender()
    })

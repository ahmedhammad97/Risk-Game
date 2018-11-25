from .model import Game
import json
from .consumer import GameConsumer

#Global Singlton Game Object
game = None


def prepare(data):
    global game
    game = Game.Game(data["map"], data["playerOne"], data["playerTwo"])

def renderMap(type, message):
    global game
    items = game.getMap()
    result =  {"type": type, "nodes": []}
    for item in items:
        result["nodes"].append(item)
        if(message!=None):
            result["message"] = message
        result["color"] = "Blue" if game.Blueturn else "Red"
    return json.dumps(result)

def startTurn():
    global game
    player = game.Blue if game.Blueturn else game.Red
    return player.deploy(game.cities, game.calculateBonus())

def completeTurn():
    global game
    player = game.Blue if game.Blueturn else game.Red
    return player.attack(game.cities)

def endturn():
    global game
    game.Blueturn = not game.Blueturn
    return checkForWinner()

def checkForWinner():
    winnerColor = game.cities[0].owner
    flag = True
    for city in game.cities:
        if city.owner != winnerColor:
            flag = False
            break
    return {"flag": flag, "winner": winnerColor}

def updateMapByHuman(data):
    global game
    player = game.Blue if game.Blueturn else game.Red
    player.update(data, game.cities)

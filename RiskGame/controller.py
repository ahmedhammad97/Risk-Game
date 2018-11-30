from .model import Game
import json
from .consumer import GameConsumer

#Global Singlton Game Object
game = None


def prepare(data): #Creates game instance
    global game
    game = Game.Game(data["map"], data["playerOne"], data["playerTwo"])

def renderMap(type, message): #Returns Json object to be rendered by client
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
    return player.deploy(game.cities, getBonus())

def completeTurn():
    global game
    player = game.Blue if game.Blueturn else game.Red
    return player.attack(game.cities)

def endturn():
    global game
    game.Blueturn = not game.Blueturn
    return checkForWinner()

def getBonus():
    return game.calculateBonus()

def getColor():
    return "Blue" if game.Blueturn else "Red"

def checkForWinner():
    winnerColor = game.cities[0].owner
    flag = True
    for city in game.cities:
        if city.owner != winnerColor: #Still have territories to attack
            flag = False
            break
    return {"flag": flag, "winner": winnerColor}

def updateMapByHuman(data): #Apply human agent moves to the model
    global game
    player = game.Blue if game.Blueturn else game.Red
    player.update(data, game.cities)

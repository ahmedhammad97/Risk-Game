from .model import Game

class controller:
    def __init__(self, data):
        #Create Model
        self.game = Game(data.map, data.playerOne, data.playerTwo)

    

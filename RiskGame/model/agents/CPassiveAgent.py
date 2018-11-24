from .. import AgentsHelper

class CPassiveAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        #Find city with minimum armies
        minimum = 999999
        minCity = None
        for city in map:
            if city.owner == self.color:
                if city.armies < minimum:
                    minimum = city.armies
                    minCity = city
        if minCity:
            minCity.armies += armies
        return AgentsHelper.sendDeployments(self.color, armies)

    def attack(self, map):
        #Do nothing
        return AgentsHelper.sendTroops(self.color)

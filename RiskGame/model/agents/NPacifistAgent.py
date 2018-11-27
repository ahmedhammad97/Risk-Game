from .. import AgentsHelper

class NPacifistAgent:
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
        #Find oppenent city with minimum armies
        minimum = 999999
        minCity = None
        for city in map:
            if city.owner != self.color:
                if city.armies < minimum:
                    for neighbour in city.neighbours:
                        if neighbour.owner == self.color:
                            if neighbour.armies > city.armies + 1:
                                city.armies = neighbour.armies - 1
                                neighbour.armies = 1
                                city.owner = self.color
                                return AgentsHelper.sendTroops(self.color)

        return AgentsHelper.sendTroops(self.color)

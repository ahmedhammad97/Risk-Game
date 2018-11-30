from .. import AgentsHelper

class AggresiveAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        maximum = 0
        maxCity = None
        for city in map:
            if city.owner == self.color: #Allied city
                if city.armies > maximum:
                    maximum = city.armies
                    maxCity = city
        if maxCity: #Found city with maximum troops
            maxCity.armies += armies

        return AgentsHelper.sendDeployments(self.color, armies)


    def attack(self, map):
        #For each city, find it's strongest neighbour
        attackedNeighbours = set() #To not attack same city multiple times
        for city in map:
            if city.owner == self.color:
                maximum = 0
                maxNeighbour = None
                for neighbour in city.neighbours:
                    if neighbour.owner != self.color:
                        if neighbour.armies < city.armies-1: #Can be attacked
                            if neighbour.armies > maximum:
                                maximum = neighbour.armies
                                maxNeighbour = neighbour

                if maxNeighbour:
                    if maxNeighbour not in attackedNeighbours:
                        maxNeighbour.armies = city.armies - maximum - 1
                        city.armies = 1
                        maxNeighbour.owner = self.color
                        attackedNeighbours.add(maxNeighbour)

        return AgentsHelper.sendTroops(self.color)

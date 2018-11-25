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
                    minimum = city.armies
                    minCity = city
        if minCity:
            #Find city with maximum armies
            strongestNumber = 0
            strongestCity = None
            for city in minCity.neighbours:
                if city.armies > strongestNumber:
                    strongestNumber = city.armies
                    strongestCity = city

            #Check if it can attack
            if strongestNumber>minimum:
                strongestCity.armies = 1
                minCity.armies = strongestNumber - minimum - 1
                minCity.owner = self.color

            return AgentsHelper.sendTroops(self.color)

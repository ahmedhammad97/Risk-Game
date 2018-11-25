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
            #Find all matches
            allMinCities = list()
            allMinCities.append(minCity)
            for city in map:
                if city.owner == self.color:
                    if city.armies == minimum:
                        allMinCities.append(city)

            for oneMinCity in allMinCities:
                #Find cities with maximum armies
                strongestNumber = 0
                strongestCity = None
                for city in minCity.neighbours:
                    if city.owner == self.color:
                        if city.armies > strongestNumber:
                            strongestNumber = city.armies
                            strongestCity = city

                #Check if it can attack
                if strongestNumber-1 > minimum:
                    strongestCity.armies = 1
                    minCity.armies = strongestNumber - minimum - 1
                    minCity.owner = self.color
                    break

        return AgentsHelper.sendTroops(self.color)

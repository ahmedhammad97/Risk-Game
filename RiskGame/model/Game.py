import random
from . import Data

class Game:
    def __init__(self, country, agentOne, agentTwo):
        #Players TBC
        self.country = country
        self.MapData = Data.EgyptCities if country=="Egypt" else Data.UsaCities
        self.cities = []
        self.constructGraph()
        self.populateNeighbours()

    def constructGraph(self):
        for i in range(len(self.MapData)):
            owner = "Blue" if random.getrandbits(1)==1 else "Red"
            node = Node(i, owner)
            self.cities.append(node)

    def populateNeighbours(self):
        for city in self.cities:
            for neighbour in self.MapData[i]:
                city.neighbours.append(self.cities[neighbour])

    def getIds(self):
        result = []
        for city in self.cities:
            result.append(city.id)

import random
from . import Data, Node, AgentFactory

class Game:
    def __init__(self, country, agentOne, agentTwo):
        self.Blue = AgentFactory.build(agentOne, "Blue")
        self.Red = AgentFactory.build(agentTwo, "Red")
        self.cities = []
        self.Blueturn = True
        self.constructGraph(country) #Generate random city distribution
        self.placeArmies() #Add random troops to the territories
        self.populateNeighbours() #Add list of neighbours to each city

    def constructGraph(self, country):
        self.MapData = Data.EgyptCities if country=="Egypt" else Data.UsaCities
        for i in range(len(self.MapData)):
            owner = "Blue" if random.getrandbits(1)==1 else "Red" #Random distribution
            node = Node.Node(i, owner)
            self.cities.append(node)

    def placeArmies(self):
        for city in self.cities:
            city.armies = random.randint(1, 5) #Random number

    def populateNeighbours(self):
        for city in self.cities:
            for neighbour in self.MapData[city.id]:
                city.neighbours.append(self.cities[neighbour])

    def getMap(self):
        for city in self.cities:
            #Generate an object for all yeilded records
            yield { "color":city.owner, "armies":city.armies }

    def calculateBonus(self):
        turn = "Blue" if self.Blueturn else "Red"
        counter = 0
        for city in self.cities:
            if city.owner == turn:
                counter+=1
        return max(3, int(counter/3))

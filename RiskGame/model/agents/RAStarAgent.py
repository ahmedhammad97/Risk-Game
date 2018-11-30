from .. import AgentsHelper

class RAStarAgent:
    def __init__(self, color):
        self.color = color
        self.cost = 0

    def deploy(self, map, armies):
        children = AgentsHelper.giveBirth(map, self.color, armies)
        minHeuristic = 999999
        self.cost += 1 #Cost represents number of turns
        for child in children:
            childHeuristic = AgentsHelper.calculateHeuristic(child["state"], self.color)
            if childHeuristic + self.cost < minHeuristic:
                minHeuristic = childHeuristic + self.cost
                self.newMap = child

        AgentsHelper.updateMap(map, self.newMap["parent"])
        return AgentsHelper.sendDeployments(self.color, armies)

    def attack(self, map):
        AgentsHelper.updateMap(map, self.newMap["state"])
        return AgentsHelper.sendTroops(self.color)

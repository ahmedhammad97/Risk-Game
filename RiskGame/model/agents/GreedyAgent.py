from .. import AgentsHelper

class GreedyAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        children = AgentsHelper.giveBirth(map, self.color, armies)
        minHeuristic = 999999
        for child in children:
            childHeuristic = AgentsHelper.calculateHeuristic(child["state"], self.color)
            if childHeuristic < minHeuristic:
                minHeuristic = childHeuristic
                self.newMap = child

        for i,city in enumerate(map):
            city.armies = self.newMap["parent"][i].armies
            city.owner = self.newMap["parent"][i].owner

        return AgentsHelper.sendDeployments(self.color, armies)

    def attack(self, map):
        for i,city in enumerate(map):
            city.armies = self.newMap["state"][i].armies
            city.owner = self.newMap["state"][i].owner

        return AgentsHelper.sendTroops(self.color)

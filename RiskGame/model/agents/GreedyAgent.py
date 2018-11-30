from .. import AgentsHelper

class GreedyAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        children = AgentsHelper.giveBirth(map, self.color, armies)
        minHeuristic = 999999
        for child in children:
            #Find state with best heuristic
            childHeuristic = AgentsHelper.calculateHeuristic(child["state"], self.color)
            if childHeuristic < minHeuristic:
                minHeuristic = childHeuristic
                self.newMap = child

        AgentsHelper.updateMap(map, self.newMap["parent"])
        return AgentsHelper.sendDeployments(self.color, armies)

    def attack(self, map):
        AgentsHelper.updateMap(map, self.newMap["state"])
        return AgentsHelper.sendTroops(self.color)

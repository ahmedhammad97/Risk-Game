from .. import AgentsHelper
from queue import PriorityQueue


class AStarAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        PQueue = PriorityQueue()
        visited = set()
        cost = 0

        children = AgentsHelper.giveBirth(map, self.color, armies)
        for child in children:
            heuristic = AgentsHelper.calculateHeuristic(child["state"], self.color)
            PQueue.put((heuristic, child["state"], child))

        while(not PQueue.empty()):
            queueItem = PQueue.get()
            state = queueItem[1]

            if cost >= 99:
                self.newMap = queueItem[2]
                for i,city in enumerate(map):
                    city.armies = self.newMap["parent"][i].armies
                    city.owner = self.newMap["parent"][i].owner
                return AgentsHelper.sendDeployments(self.color, armies)

            tupleState = tuple(state)
            if tupleState in visited: #Visited before
                continue
            visited.add(tupleState)

            if AgentsHelper.isGoalState(state, self.color):
                self.newMap = queueItem[2]
                for i,city in enumerate(map):
                    city.armies = self.newMap["parent"][i].armies
                    city.owner = self.newMap["parent"][i].owner
                return AgentsHelper.sendDeployments(self.color, armies)

            newArmies = AgentsHelper.calculateBonus(state, self.color)
            children = AgentsHelper.giveBirth(state, self.color, newArmies)
            cost += 1
            for child in children:
                heuristic = AgentsHelper.calculateHeuristic(child["state"], self.color)
                PQueue.put((heuristic + cost, child["state"], queueItem[2]))


    def attack(self, map):
        for i,city in enumerate(map):
            city.armies = self.newMap["state"][i].armies
            city.owner = self.newMap["state"][i].owner

        return AgentsHelper.sendTroops(self.color)

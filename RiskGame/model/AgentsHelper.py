from .. import controller
from copy import deepcopy

def sendDeployments(owner, armies):
    type = "renderDeployments"
    message = owner + " has " + str(armies) + " to deploy"
    return controller.renderMap(type, message)

def sendTroops(owner):
    type = "renderAttack"
    message = owner + " is attacking..."
    return controller.renderMap(type, message)

def calculateHeuristic(map, color):
    counter = 0
    for city in map:
        if city.owner != color:
            counter+=city.armies
    return counter

def isGoalState(map, color):
    for city in map:
        if city.owner != color:
            return False
    return True

def giveBirth(map, color, armies):
    deploymentOffspring = list()
    for i,city in enumerate(map):
        if city.owner == color: #We can deploy
            offspring = deepcopy(map)
            offspring[i].armies += armies
            deploymentOffspring.append(offspring)

    attackinfOffspring = list()
    for state in deploymentOffspring:
        for i,city in enumerate(state):
            if city.owner == color: #We can attack by
                for k,neighbour in enumerate(city.neighbours):
                    if neighbour.owner != color:
                        if neighbour.armies < city.armies -1:
                            offspring = deepcopy(state)
                            offspring[i][k].armies = offspring[i].armies - 1
                            offspring[i].armies = 1
                            attackinfOffspring.append({
                                "parent" : state,
                                "state" : offspring
                            })

    return attackinfOffspring

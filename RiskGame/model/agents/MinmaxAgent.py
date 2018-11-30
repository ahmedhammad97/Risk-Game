from .. import AgentsHelper

class MinmaxAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        children = AgentsHelper.giveBirth(map, self.color, armies) #Generate next level of states
        for child in children:
            output = self.minmax(child["state"], armies, 1, -999999, 999999, True, child)
            self.newMap = output[1]

        AgentsHelper.updateMap(map, self.newMap["parent"])
        return AgentsHelper.sendDeployments(self.color, armies)

    def minmax(self, state, armies, depth, alpha, beta, isMaximumTurn, toReturn):
        #Check for termination
        if depth == 0 or AgentsHelper.isGoalState(state, self.color):
            heuristic = AgentsHelper.calculateHeuristic(state, self.color)
            return (heuristic, toReturn)

        if isMaximumTurn: #This player turn
            maximumHeuristic = (-999999, None)
            nextStates = AgentsHelper.giveBirth(state, self.color, armies)

            for nextState in nextStates:
                newArmies = AgentsHelper.calculateBonus(nextState["state"], self.color)
                nextStateResult = self.minmax(nextState["state"], newArmies, depth-1, alpha, beta, False, toReturn)

                #Compare for maximum heuristic
                if nextStateResult[0] > maximumHeuristic[0]:
                    maximumHeuristic = nextStateResult

                #Update alpha
                if nextStateResult[0] > alpha:
                    alpha = nextStateResult[0]

                #Check for pruning chance
                if alpha >= beta:
                    break #No hope of a better results

            return (maximumHeuristic[0], toReturn)

        else: #Opponent turn
            minimumHeuristic = (999999, None)
            nextStates = AgentsHelper.giveBirth(state, self.color, armies)

            for nextState in nextStates:
                newArmies = AgentsHelper.calculateBonus(nextState["state"], self.color)
                nextStateResult = self.minmax(nextState["state"], newArmies, depth-1, alpha, beta, True, toReturn)

                #Compare for minimum heuristic
                if nextStateResult[0] < minimumHeuristic[0]:
                    minimumHeuristic = nextStateResult

                #Update beta
                if nextStateResult[0] < beta:
                    beta = nextStateResult[0]

                #Check for pruning chance
                if alpha >= beta:
                    break #No hope of a better results

            return (minimumHeuristic[0], toReturn)



    def attack(self, map):
        AgentsHelper.updateMap(map, self.newMap["state"])
        return AgentsHelper.sendTroops(self.color)

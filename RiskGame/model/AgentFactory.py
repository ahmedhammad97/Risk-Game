from .agents import HumanAgent, CPassiveAgent, AggresiveAgent
from .agents import NPacifistAgent, GreedyAgent, AStarAgent
from .agents import RAStarAgent, MinmaxAgent

def build(agentName, playerColor):
    try:
        #Python way of doing switch-case
        return {
            "human": HumanAgent.HumanAgent(playerColor),
            "cPassive": CPassiveAgent.CPassiveAgent(playerColor),
            "aggresive": AggresiveAgent.AggresiveAgent(playerColor),
            "nPacifist": NPacifistAgent.NPacifistAgent(playerColor),
            "greedy": GreedyAgent.GreedyAgent(playerColor),
            "aStar": AStarAgent.AStarAgent(playerColor),
            "rAStar": RAStarAgent.RAStarAgent(playerColor),
            "minmax": MinmaxAgent.MinmaxAgent(playerColor)
        }.get(agentName)
    except Exception as e:
        print(e)

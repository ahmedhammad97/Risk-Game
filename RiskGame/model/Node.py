
class Node:
    def __init__(self, id, owner, armies=0):
        self.id = id
        self.owner = owner
        self.armies = armies
        self.neighbours = []

    def __lt__(self, other): #Comparison fn used by PriorityQueue
        return 1

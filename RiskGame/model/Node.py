

class Node:
    def __init__(self, id, owner, armies=0):
        self.id = id
        self.owner = owner
        self.armies = armies
        self.neighbours = []

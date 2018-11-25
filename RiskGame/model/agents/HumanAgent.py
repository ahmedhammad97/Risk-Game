from .. import AgentsHelper

class HumanAgent:
    def __init__(self, color):
        self.color = color

    def deploy(self, map, armies):
        return "HumanDeploy"

    def attack(self, map):
        pass

    def update(self, data, map):
        updates = data.updates
        for record in updates:
            city = map[int(record["id"])]
            city.armies = int(record["armies"])
            city.owner = record["color"]

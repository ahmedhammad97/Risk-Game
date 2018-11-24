from .. import controller

def sendDeployments(owner, armies):
    type = "renderDeployments"
    message = owner + " has " + armies + " to deploy"
    controller.renderMap(type, message)

def sendTroops(owner):
    type = "renderAttack"
    message = owner + " is attacking..."
    controller.renderMap(type, message)

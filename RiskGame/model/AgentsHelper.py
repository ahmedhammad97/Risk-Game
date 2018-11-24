from .. import consumer, controller

def sendDeployments(owner, armies):
    type = "renderDeployments"
    message = owner + " has " + str(armies) + " to deploy"
    return controller.renderMap(type, message)

def sendTroops(owner):
    type = "renderAttack"
    message = owner + " is attacking..."
    return controller.renderMap(type, message)

def humanDeploy():
    consumer.GameConsumer.requestDeploy()

def humanAttack():
    consumer.GameConsumer.requestAttack()

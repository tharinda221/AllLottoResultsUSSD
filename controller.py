from datetime import timedelta
from flask import *
from flask_restful import *
from core.transportmgt.ideamart.receiveMessage import *
from core.transportmgt.ideamart.caas.CAASNotification import *
from core.transportmgt.ideamart.sendMessageToAllSubscribers.sendMessageToAll import *

app = Flask(__name__)
api = Api(app)

api.add_resource(ReceiveMessage, '/ussdReceiver')
api.add_resource(CASSNotification, '/caasNotification')
api.add_resource(sendMessageToAll, '/sendMessageToAll/<message>')

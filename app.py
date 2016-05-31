from flask import *
from flask_restful import *
from core.transportmgt.ideamart.receiveMessage import *

app = Flask(__name__)
api = Api(app)

api.add_resource(ReceiveMessage, '/smsReceiver')
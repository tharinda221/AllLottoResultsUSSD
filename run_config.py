from datetime import timedelta
from flask import *
from flask_restful import *
from core.transportmgt.ideamart.receiveMessage import *


app = Flask(__name__)
api = Api(app)

api.add_resource(ReceiveMessage, '/ussdReceiver')


@app.route('/')
def error():
    logging.error("Download Log File")
    return send_from_directory("","/var/log/apache2/error.log")
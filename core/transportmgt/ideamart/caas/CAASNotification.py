import logging

from __init__ import *

class CASSNotification(Resource):
    def get(self):
        logging.error("Telco App is running")
        logging.error(request.data)
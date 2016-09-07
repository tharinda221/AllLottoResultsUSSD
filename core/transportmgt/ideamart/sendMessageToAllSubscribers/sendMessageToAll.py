from __init__ import *
from core.applicationmgt.Application import *

class sendMessageToAll(Resource):
    def get(self, message):
        sendMessageToAllUsers(message)
        response = make_response("message was sent")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response

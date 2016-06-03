from __init__ import *
from core.applicationmgt.Application import *

class ReceiveMessage(Resource):
    def get(self):
        logging.error("Telco App is running")
        logging.error(request.data)
        response = make_response("Telco App is running")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response

    def post(self):
        logging.error("POST Request Came")
        logging.error("\n\n**** HTTP Request:\n" + request.data + "****\n\n")
        received_content = request.data
        decoded_json = json.loads(received_content)
        AllLotto(decoded_json)
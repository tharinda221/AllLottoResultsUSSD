from __init__ import *
from core.applicationmgt.Application import *

class ReceiveMessage(Resource):
    def get(self):
        response = make_response("Telco USSD App is running")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response

    def post(self):
        received_content = request.data
        decoded_json = json.loads(received_content)
        AllLotto(decoded_json)

class SMSReceive(Resource):
    def get(self):
        logging.error("Telco App is running")
        logging.error(request.data)
        response = make_response("Telco SMS App is running")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response

    def post(self):
        logging.error("POST Request Came to SMS")
        logging.error("\n\n**** HTTP Request:\n" + request.data + "****\n\n")
        received_content = request.data
        decoded_json = json.loads(received_content)
        logging.error("SMS number")
        logging.error(decoded_json["sourceAddress"])
        SMSMessage = SMSmessageBody(message=Application.initSMS, password=Ideamart.password, url=Ideamart.SMSUrl,
                                    destAddress=decoded_json["sourceAddress"],
                                    applicationID=decoded_json["applicationId"])
        sendSMSMessage(SMSMessage)

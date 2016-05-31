import logging

from __init__ import *


class ReceiveMessage(Resource):
    def get(self):
        logging.info(request.data)
        response = make_response("Hello, Telco App is running")
        response.headers['Content-Type'] = 'application/json'
        response.headers['Accept'] = 'application/json'
        return response

    def post(self):
        logging.info("\n\n**** HTTP Request:\n" + request.data + "****\n\n")
        received_content = request.data
        decoded_json = json.loads(received_content)
        if decoded_json["ussdOperation"] == "mo-init":
            message = USSDmessageBody(message="hello world!", password=Ideamart.password, url=Ideamart.USSDUrl,
                                     destAddress=decoded_json["sourceAddress"], applicationID=decoded_json["applicationId"]
                                      ,encording=decoded_json["encoding"],sessionId=decoded_json["sessionId"],
                                      ussdOperation="mo-cont",version=decoded_json["version"])
            sendUSSDMessage(message)

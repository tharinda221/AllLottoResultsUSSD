from __init__ import *


def getMessage(nlbList, dlbList):
    count = 1
    output = ""
    for nlb in nlbList.keys():
        output += str(count) + "." + nlb + "\n"
        count += 1
    for dlb in dlbList.keys():
        output += str(count) + "." + dlb + "\n"
        count += 1
    return output


def LotteryResult(number, dn):
    number -= 1
    if 0 <= number < Application.nlbListSize:
        out = getNLBResult(dn, number, Application.nlbList)
        return out
    else:
        out = getDLBResult(dn, number - Application.nlbListSize, Application.dlbList)
        return out


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
        if decoded_json["ussdOperation"] == "mo-init":
            Application.nlbList = getDataFromNLB()
            Application.nlbListSize = len(Application.nlbList)
            Application.dlbList = getDataFromDLB()
            Application.dlbListSize = len(Application.dlbList)
            message = getMessage(Application.nlbList, Application.dlbList)
            logging.error(message)
            USSDmessage = USSDmessageBody(message="message",
                                          password=Ideamart.password, url=Ideamart.USSDUrl,
                                          destAddress=decoded_json["sourceAddress"],
                                          applicationID=decoded_json["applicationId"]
                                          , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                          ussdOperation="mt-cont", version=decoded_json["version"])
            SMSmessage = SMSmessageBody(message="hello world!", password=Ideamart.password, url=Ideamart.SMSUrl,
                                        destAddress=decoded_json["sourceAddress"],
                                        applicationID=decoded_json["applicationId"])
            sendUSSDMessage(USSDmessage)
            #sendSMSMessage(SMSmessage)
            Application.messageFlow = 1
        else:
            logging.error("mo-cont Request Came")
            try:
                requestNumber = int(decoded_json["message"])
                if requestNumber == 0:
                    Application.messageFlow -= 2
                if Application.messageFlow == 0:
                    USSDmessage = USSDmessageBody(message=getMessage(Application.nlbList, Application.dlbList),
                                                  password=Ideamart.password, url=Ideamart.USSDUrl,
                                                  destAddress=decoded_json["sourceAddress"],
                                                  applicationID=decoded_json["applicationId"]
                                                  , encording=decoded_json["encoding"],
                                                  sessionId=decoded_json["sessionId"],
                                                  ussdOperation="mt-cont", version=decoded_json["version"])
                    sendUSSDMessage(USSDmessage)
                    Application.messageFlow = 1
                elif Application.messageFlow == 1:
                    if (1 <= int(decoded_json["message"]) <= (Application.dlbListSize + Application.nlbListSize)):
                        Application.index = requestNumber
                        USSDmessage = USSDmessageBody(message=Application.getDrawNumber,
                                                      password=Ideamart.password, url=Ideamart.USSDUrl,
                                                      destAddress=decoded_json["sourceAddress"],
                                                      applicationID=decoded_json["applicationId"]
                                                      , encording=decoded_json["encoding"],
                                                      sessionId=decoded_json["sessionId"],
                                                      ussdOperation="mt-cont", version=decoded_json["version"])
                        sendUSSDMessage(USSDmessage)
                        Application.messageFlow += 1
                    else:
                        USSDmessage = USSDmessageBody(message=Application.ErrorMessage,
                                                      password=Ideamart.password, url=Ideamart.USSDUrl,
                                                      destAddress=decoded_json["sourceAddress"],
                                                      applicationID=decoded_json["applicationId"]
                                                      , encording=decoded_json["encoding"],
                                                      sessionId=decoded_json["sessionId"],
                                                      ussdOperation="mt-cont", version=decoded_json["version"])
                        sendUSSDMessage(USSDmessage)
                        Application.messageFlow -= 1
                elif Application.messageFlow == 2:
                    USSDmessage = USSDmessageBody(message=LotteryResult(Application.index, str(
                        requestNumber)) + "\n" + "0. Thava balanna" + "\n" + "99. Exit",
                                                  password=Ideamart.password, url=Ideamart.USSDUrl,
                                                  destAddress=decoded_json["sourceAddress"],
                                                  applicationID=decoded_json["applicationId"]
                                                  , encording=decoded_json["encoding"],
                                                  sessionId=decoded_json["sessionId"],
                                                  ussdOperation="mt-cont", version=decoded_json["version"])
                    sendUSSDMessage(USSDmessage)

            except:
                USSDmessage = USSDmessageBody(message=Application.ErrorMessage,
                                              password=Ideamart.password, url=Ideamart.USSDUrl,
                                              destAddress=decoded_json["sourceAddress"],
                                              applicationID=decoded_json["applicationId"]
                                              , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                              ussdOperation="mt-cont", version=decoded_json["version"])
                sendUSSDMessage(USSDmessage)
                Application.messageFlow -= 1

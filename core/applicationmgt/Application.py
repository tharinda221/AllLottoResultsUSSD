from __init__ import *

from core.usermgt.User import User
from core.usermgt.UserDAO import UserDAO


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


def AllLotto(decoded_json):
    # user DAO initiated
    dao = UserDAO()
    # identifying initial request came from user
    if decoded_json["ussdOperation"] == "mo-init":
        # fetch data from lottery database
        Application.nlbList = getDataFromNLB()
        Application.nlbListSize = len(Application.nlbList)
        Application.dlbList = getDataFromDLB()
        Application.dlbListSize = len(Application.dlbList)
        message = getMessage(Application.nlbList, Application.dlbList)
        # initiate the user object
        user = User(address=decoded_json["sourceAddress"], index=0, messageFlow=1, lotteryList=[],
                    count=1)
        dao.createUser(user)
        USSDmessage = USSDmessageBody(message=message,
                                      password=Ideamart.password, url=Ideamart.USSDUrl,
                                      destAddress=decoded_json["sourceAddress"],
                                      applicationID=decoded_json["applicationId"]
                                      , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                      ussdOperation="mt-cont", version=decoded_json["version"])
        sendUSSDMessage(USSDmessage)
    #
    else:
        logging.error("mo-cont Request Came")

        if decoded_json["message"] == "000":
            USSDmessage = USSDmessageBody(message=Application.EndMessage,
                                          password=Ideamart.password, url=Ideamart.USSDUrl,
                                          destAddress=decoded_json["sourceAddress"],
                                          applicationID=decoded_json["applicationId"]
                                          , encording=decoded_json["encoding"],
                                          sessionId=decoded_json["sessionId"],
                                          ussdOperation="mt-fin", version=decoded_json["version"])
            sendUSSDMessage(USSDmessage)
        else:
            try:
                requestNumber = int(decoded_json["message"])
                user = dao.getUser(decoded_json["sourceAddress"])
                Application.messageFlow = user.messageFlow
                logging.error("messageFlow")
                logging.error(Application.messageFlow)
                if (requestNumber == 0) and (Application.messageFlow) == 2:
                    Application.messageFlow = 0
                if Application.messageFlow == 0:
                    # fetch data from lottery database
                    Application.nlbList = getDataFromNLB()
                    Application.nlbListSize = len(Application.nlbList)
                    Application.dlbList = getDataFromDLB()
                    Application.dlbListSize = len(Application.dlbList)
                    message = getMessage(Application.nlbList, Application.dlbList)

                    USSDmessage = USSDmessageBody(message=message,
                                                  password=Ideamart.password, url=Ideamart.USSDUrl,
                                                  destAddress=decoded_json["sourceAddress"],
                                                  applicationID=decoded_json["applicationId"]
                                                  , encording=decoded_json["encoding"],
                                                  sessionId=decoded_json["sessionId"],
                                                  ussdOperation="mt-cont", version=decoded_json["version"])
                    sendUSSDMessage(USSDmessage)
                    dao.updateUserMessageFlow(decoded_json["sourceAddress"], 1)
                # request draw number
                elif Application.messageFlow == 1:
                    logging.error("requestNumber")
                    logging.error(requestNumber)
                    # fetch data from lottery database
                    Application.nlbList = getDataFromNLB()
                    Application.nlbListSize = len(Application.nlbList)
                    Application.dlbList = getDataFromDLB()
                    Application.dlbListSize = len(Application.dlbList)

                    if (0 < requestNumber <= (Application.dlbListSize + Application.nlbListSize)):
                        dao.updateUserIndex(decoded_json["sourceAddress"], requestNumber)
                        USSDmessage = USSDmessageBody(message=Application.getDrawNumber,
                                                      password=Ideamart.password, url=Ideamart.USSDUrl,
                                                      destAddress=decoded_json["sourceAddress"],
                                                      applicationID=decoded_json["applicationId"]
                                                      , encording=decoded_json["encoding"],
                                                      sessionId=decoded_json["sessionId"],
                                                      ussdOperation="mt-cont", version=decoded_json["version"])
                        sendUSSDMessage(USSDmessage)
                        dao.updateUserMessageFlow(decoded_json["sourceAddress"], 2)
                    # user request fail scenario
                    else:
                        USSDmessage = USSDmessageBody(message=Application.ErrorMessage,
                                                      password=Ideamart.password, url=Ideamart.USSDUrl,
                                                      destAddress=decoded_json["sourceAddress"],
                                                      applicationID=decoded_json["applicationId"]
                                                      , encording=decoded_json["encoding"],
                                                      sessionId=decoded_json["sessionId"],
                                                      ussdOperation="mt-cont", version=decoded_json["version"])
                        sendUSSDMessage(USSDmessage)
                        dao.updateUserMessageFlow(decoded_json["sourceAddress"], 0)
                        # send result message
                elif Application.messageFlow == 2:
                    # fetch data from lottery database
                    Application.nlbList = getDataFromNLB()
                    Application.nlbListSize = len(Application.nlbList)
                    Application.dlbList = getDataFromDLB()
                    Application.dlbListSize = len(Application.dlbList)
                    result = LotteryResult(user.index, str(requestNumber))
                    result = result.replace('\xc2\xa0', ' ')
                    logging.error("Result")
                    logging.error(result)
                    USSDmessage = USSDmessageBody(message= result + "\n" + "0. Thava balanna" + "\n" + "000. Exit",
                                                  password=Ideamart.password, url=Ideamart.USSDUrl,
                                                  destAddress=decoded_json["sourceAddress"],
                                                  applicationID=decoded_json["applicationId"]
                                                  , encording=decoded_json["encoding"],
                                                  sessionId=decoded_json["sessionId"],
                                                  ussdOperation="mt-cont", version=decoded_json["version"])
                    sendUSSDMessage(USSDmessage)
                    dao.updateUserMessageFlow(decoded_json["sourceAddress"], 0)
            # This exceptional is to handle bad request came by the user such as strings.
            except:
                USSDmessage = USSDmessageBody(message=Application.ErrorMessage,
                                              password=Ideamart.password, url=Ideamart.USSDUrl,
                                              destAddress=decoded_json["sourceAddress"],
                                              applicationID=decoded_json["applicationId"]
                                              , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                              ussdOperation="mt-cont", version=decoded_json["version"])
                sendUSSDMessage(USSDmessage)
                dao.updateUserMessageFlow(decoded_json["sourceAddress"], 0)

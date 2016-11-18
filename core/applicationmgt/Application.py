from __init__ import *

from core.usermgt.User import User
from core.usermgt.UserDAO import UserDAO
import random

privateNumbers = ["tel:AZ110N9CCX6oc2Vqnw+UnDAzB6SJcMF5CkK2UOEgTR2KwfaZ4KDZcwNDIq8viBORtMF6j",
            "tel:B%3C4mM3G8otswwsxt84tttry45JlO+MJQgz+kJXOiRgandOzuHzjyfZM+Y2ake+ExryL"]
# "tel:B%3C4mM3G8otswwsxt84tttry45JlO+MJQgz+kJXOiRgandNiOoeb2KN1wLxBRD6LLcPh"
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


def getExternalTrxId():
    Min = 1000000
    Max = 2000000
    return Min + (int)(random.random() * ((Max - Min) + 1))


def sendMessageToAllUsers(message, address):
    SMSMessage = SMSmessageBody(message=message, password=Ideamart.password, url=Ideamart.SMSUrl,
                                destAddress=address,
                                applicationID=Ideamart.appId)
    sendSMSMessage(SMSMessage)


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
        # initiate the user object
        userExist = dao.userExist(decoded_json["sourceAddress"])
        if userExist:
            dao.updateUserElder(decoded_json["sourceAddress"], "False")
        else:
            user = User(address=decoded_json["sourceAddress"], index=0, messageFlow=1, lotteryList=[],
                        count=1, newUser="True")
            dao.createUser(user)

        subscriptionstatus = SubscriptionStatusBody(subscriberId=decoded_json["sourceAddress"],
                                                    password=Ideamart.password,
                                                    applicationID=decoded_json["applicationId"],
                                                    url=Ideamart.SubscriptionStatusUrl)
        if getSubscriptionStatus(subscriptionstatus):
            message = getMessage(Application.nlbList, Application.dlbList)
            USSDmessage = USSDmessageBody(message=message,
                                          password=Ideamart.password, url=Ideamart.USSDUrl,
                                          destAddress=decoded_json["sourceAddress"],
                                          applicationID=decoded_json["applicationId"]
                                          , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                          ussdOperation="mt-cont", version=decoded_json["version"])


            sendUSSDMessage(USSDmessage)
            if decoded_json["sourceAddress"] not in privateNumbers:
                CAASmessage = CAASmessageBody(password=Ideamart.password, url=Ideamart.CAASUrl,
                                              SubscriberId=decoded_json["sourceAddress"],
                                              applicationID=decoded_json["applicationId"],
                                              ExternalTrxId=getExternalTrxId(),
                                              Amount=Ideamart.Amount)
                sendCAASMessage(CAASmessage)
        else:
            dao.updateUserElder(decoded_json["sourceAddress"], "True")
            USSDmessage = USSDmessageBody(message=Application.regMessage,
                                          password=Ideamart.password, url=Ideamart.USSDUrl,
                                          destAddress=decoded_json["sourceAddress"],
                                          applicationID=decoded_json["applicationId"]
                                          , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                          ussdOperation="mt-cont", version=decoded_json["version"])

            sendUSSDMessage(USSDmessage)
    #
    else:

        user = dao.getUser(decoded_json["sourceAddress"])
        # fetch data from lottery database
        Application.nlbList = getDataFromNLB()
        Application.nlbListSize = len(Application.nlbList)
        Application.dlbList = getDataFromDLB()
        Application.dlbListSize = len(Application.dlbList)
        message = getMessage(Application.nlbList, Application.dlbList)
        if (user.newUser == "True"):
            USSDmessage = USSDmessageBody(message=message,
                                          password=Ideamart.password, url=Ideamart.USSDUrl,
                                          destAddress=decoded_json["sourceAddress"],
                                          applicationID=decoded_json["applicationId"]
                                          , encording=decoded_json["encoding"], sessionId=decoded_json["sessionId"],
                                          ussdOperation="mt-cont", version=decoded_json["version"])
            # user subscription
            SubscriptionMessage = SubscriptionMessageBody(subscriberId=decoded_json["sourceAddress"],
                                                          password=Ideamart.password, url=Ideamart.SubscriptionUrl,
                                                          applicationID=decoded_json["applicationId"], action="1",
                                                          version=decoded_json["version"])
            sendSubscriptionMessage(SubscriptionMessage)
            sendUSSDMessage(USSDmessage)
            if decoded_json["sourceAddress"] not in privateNumbers:
                CAASmessage = CAASmessageBody(password=Ideamart.password, url=Ideamart.CAASUrl,
                                              SubscriberId=decoded_json["sourceAddress"],
                                              applicationID=decoded_json["applicationId"],
                                              ExternalTrxId=getExternalTrxId(),
                                              Amount=Ideamart.Amount)
                sendCAASMessage(CAASmessage)
            dao.updateUserMessageFlow(decoded_json["sourceAddress"], 1)
            dao.updateUserElder(decoded_json["sourceAddress"], "False")
            sendsms = SMSmessageBody(message=Application.initSMS,
                                     password=Ideamart.password,url=Ideamart.SMSUrl,destAddress=decoded_json["sourceAddress"],
                                          applicationID=decoded_json["applicationId"])
            sendSMSMessage(sendsms)
            return

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
                if (requestNumber == 0) and (Application.messageFlow) == 2:
                    Application.messageFlow = 0
                if Application.messageFlow == 0:

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
                    USSDmessage = USSDmessageBody(message=result + "\n" + "0. Thava balanna" + "\n" + "000. Exit",
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

import logging
import urllib2
from flask import json


def sendSubscriptionMessage(messageBody):
    res = {'applicationId': messageBody.applicationID,
           "password": messageBody.password,
           "version": messageBody.version,
           "action": messageBody.action,
           "subscriberId": messageBody.subscriberId
           }

    logging.error("Print Subscription payload")
    logging.error(json.dumps(res))
    req = urllib2.Request(messageBody.url, data=json.dumps(res),
                          headers={"Content-Type": "application/json", "Accept": "application/json"})
    response = urllib2.urlopen(req)
    result = response.read()
    logging.error("subscription result")
    logging.error(result)
    jsonResult = json.loads(result)
    print result

    if response.getcode() == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(response.getcode()) + ' ****')
    return jsonResult["statusDetail"]


def getSubscriptionStatus(messageBody):
    res = {'applicationId': messageBody.applicationID,
           "password": messageBody.password,
           "subscriberId": messageBody.subscriberId
           }
    req = urllib2.Request(messageBody.url, data=json.dumps(res),
                          headers={"Content-Type": "application/json", "Accept": "application/json"})


    response = urllib2.urlopen(req)
    result = response.read()
    logging.error("subscription status came from IdeaMart")
    logging.error(result)
    jsonResult = json.loads(result)

    if response.getcode() == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(response.getcode()) + ' ****')
    logging.error("subscriptionStatus")
    logging.error(jsonResult["subscriptionStatus"])
    return jsonResult["subscriptionStatus"] == "REGISTERED"
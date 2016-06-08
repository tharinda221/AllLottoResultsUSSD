import urllib
import urllib2

from flask import json
import logging


def sendCAASMessage(messageBody):
    res = {'applicationId': messageBody.applicationID,
           "password": messageBody.password,
           "externalTrxId": messageBody.ExternalTrxId,
           "subscriberId": messageBody.SubscriberId,
           "amount": messageBody.Amount
           }
    logging.error("Print payload")
    logging.error(json.dumps(res))
    req = urllib2.Request(messageBody.url, data=json.dumps(res), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response = urllib2.urlopen(req)
    result = response.read()
    logging.error("Result content")
    logging.error(result)

    if response.getcode() == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(response.getcode()) + ' ****')

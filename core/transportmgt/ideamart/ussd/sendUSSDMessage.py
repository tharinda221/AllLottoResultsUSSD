import urllib
import urllib2

from flask import json
import logging


def sendUSSDMessage(messageBody):
    res = {'message': messageBody.message,
           "destinationAddress": messageBody.destAddress,
           "password": messageBody.password,
           "applicationId": messageBody.applicationID,
           "ussdOperation": messageBody.ussdOperation,
           "sessionId": messageBody.sessionId,
           "encoding": messageBody.encording,
           "version": messageBody.version
           }
    req = urllib2.Request(messageBody.url, data=json.dumps(res), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response = urllib2.urlopen(req)
    result = response.read()
    logging.error("USSD response from ideamart")
    logging.error(result)

    if response.getcode() == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(response.getcode()) + ' ****')

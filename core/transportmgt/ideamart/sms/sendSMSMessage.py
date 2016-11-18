import logging
import urllib2
from flask import json


def sendSMSMessage(messageBody):
    destAddresses = []
    destAddresses.append(messageBody.destAddress)
    res = {'message': messageBody.message,
           "destinationAddresses": destAddresses,
           "password": messageBody.password,
           "applicationId": messageBody.applicationID
           }
    logging.error("SMS body")
    logging.error(res)
    req = urllib2.Request(messageBody.url, data=json.dumps(res),
                          headers={"Content-Type": "application/json", "Accept": "application/json"})
    logging.error("SMS request")
    response = urllib2.urlopen(req)
    result = response.read()
    logging.error("Result content")
    logging.error(result)

    if response.getcode() == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(response.getcode()) +  ' ****')

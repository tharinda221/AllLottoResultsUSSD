import urllib
import urllib2

import requests
from flask import json
import logging
import run_config


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
    # form_data = json.dumps(res)
    logging.error("Print payload")
    # logging.error(form_data)
    logging.error("url: " + messageBody.url)
    #data = urllib.urlencode(res)
    req = urllib2.Request(messageBody.url, data=json.dumps(res), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response = urllib2.urlopen(req)
    result = response.read()
    # result = requests.post(url=messageBody.url, data=form_data)
    logging.error("Result content")
    logging.error(result)

    if response.getcode() == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(response.getcode()) + ' ****')

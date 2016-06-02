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
    form_data = json.dumps(res)
    logging.error("Print payload")
    logging.error(form_data)
    result = requests.post(url=messageBody.url, data=form_data)

    logging.error(result.content)

    if result.status_code == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(result.status_code) + ' ****')

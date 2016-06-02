import logging

import run_config

import requests
from flask import json


def sendSMSMessage(messageBody):
    res = {'message': messageBody.message,
           "destinationAddress": messageBody.destAddress,
           "password": messageBody.password,
           "applicationId": messageBody.applicationID
           }

    logging.error(res)
    form_data = json.dumps(res)
    # logging.info(form_data)
    result = requests.post(url=messageBody.url, data=form_data)
    logging.error("SMS result")
    logging.error(result.content)

    if result.status_code == 200:
        logging.error('*** Message delivered Successfully! ****')
    else:
        logging.error('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(result.status_code) +  ' ****')

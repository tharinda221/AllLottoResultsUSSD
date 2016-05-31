from flask import json

from messageBody import messageBody
import logging
import requests


def sendMessage(messageBody):
    res = {'message': messageBody.message,
           "destinationAddresses": messageBody.destAddress,
           "password": messageBody.password,
           "applicationId": messageBody.applicationID
           }

    logging.info(res)
    form_data = json.dumps(res)
    logging.info(form_data)
    result = requests.post(url=messageBody.url, data=form_data)

    logging.info(result.content)

    if result.status_code == 200:
        logging.info('*** Message delivered Successfully! ****')
    else:
        logging.info('*** Message was not delivered Successfully!! ERROR-CODE: ' + result.status_code + ' ****')




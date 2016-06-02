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

    run_config.app.logger.info(res)
    form_data = json.dumps(res)
    # logging.info(form_data)
    result = requests.post(url=messageBody.url, data=form_data)

    run_config.app.logger.info(result.content)

    if result.status_code == 200:
        run_config.app.logger.info('*** Message delivered Successfully! ****')
    else:
        run_config.app.logger.info('*** Message was not delivered Successfully!! ERROR-CODE: ' + str(result.status_code) + ' ****')

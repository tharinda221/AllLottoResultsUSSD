# configure the app
import os
from datetime import timedelta
from controller import *
import logging
from logging import Formatter, FileHandler

app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.debug = True
app.root = os.path.abspath(os.path.dirname(__file__))
# file_handler = FileHandler('logger.log')
# file_handler.setLevel(logging.DEBUG)
# app.logger.addHandler(file_handler)

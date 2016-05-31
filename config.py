# configure the app
import os

from datetime import timedelta

from app import *

app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.debug = True
app.root = os.path.abspath(os.path.dirname(__file__))
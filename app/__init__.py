from flask import Flask
from .config import DevelopmentConfiguration
from .config import ProductionConfiguration
from flask_restful import Api

import os

application = Flask(__name__)

if 'APP_ENV' in os.environ and os.environ['APP_ENV'] == 'DEVELOPMENT':
    application.config.from_object(DevelopmentConfiguration)
else:
    application.config.from_object(ProductionConfiguration)

api = Api(application)

from . import routes
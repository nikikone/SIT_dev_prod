import os
from .enviroment_status import Enviroment
Enviroment(os.getenv('APP_ENV'))
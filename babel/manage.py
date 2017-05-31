import logging
import requests
from flask import current_app
from flask_script import Manager
from application.main import app

log = logging.getLogger(__name__)
manager = Manager(app)


if __name__ == "__main__":
    manager.run()

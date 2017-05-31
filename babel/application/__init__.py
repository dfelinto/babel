import logging.config
import os
from flask import Flask

log = logging.getLogger(__name__)
from flask_babel import Babel

# App init and configuration
app = Flask(__name__)

# Load configuration from three different sources, to make it easy to override
# settings with secrets, as well as for development & testing.
app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.config.from_pyfile(os.path.join(app_root, 'config.py'), silent=False)
app.config.from_pyfile(os.path.join(app_root, 'config_local.py'), silent=True)

# Configure logging
logging.config.dictConfig(app.config['LOGGING'])
log = logging.getLogger(__name__)
if app.config['DEBUG']:
    log.info('Babel starting, debug=%s', app.config['DEBUG'])

babel = Babel(app)

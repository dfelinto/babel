import logging
from application.main import app as application


log = logging.getLogger(__name__)


if __name__ == '__main__':
    application.run()

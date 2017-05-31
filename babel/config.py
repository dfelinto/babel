# -*- coding: utf-8 -*-
import os.path

TITLE = 'Babel'
APP_DIR = os.path.dirname(os.path.realpath(__file__))
APPLICATION_ROOT = ''  # Modify if we run on a subdomain, line /babel

# See https://docs.python.org/2/library/logging.config.html#configuration-dictionary-schema
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)-15s %(levelname)8s %(name)s %(message)s'}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stderr',
        }
    },
    'loggers': {
        'application': {'level': 'INFO'},
        'werkzeug': {'level': 'INFO'},
    },
    'root': {
        'level': 'WARNING',
        'handlers': [
            'console',
        ],
    }
}

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
    'it': 'Italiano',
    'pt': 'Portuguese',
}

import logging
from flask import abort, jsonify, render_template, request
import datetime
from . import app
from . import babel

from flask.ext.babel import gettext

from config import LANGUAGES

log = logging.getLogger(__name__)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())


def get_or_404(item_class, **query):
    try:
        item = item_class.get(**query)
    except item_class.DoesNotExist:
        return abort(404)
    return item


@app.route('/hello/<name>')
def hello(name):
    """Meet and greet function"""
    return gettext("Hello dear %(name)s, how are you?", name=name.title())


@app.route('/')
def dashboard():
    return render_template('dashboard.pug')

#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Configuration Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request(login_as: int = None):
    """ Request of each function
    """
    user: dict = get_user()
    g.user = user


def get_user() -> Union[dict, None]:
    """ Get the user of the dict

        Return User
    """
    login_user = request.args.get('login_as', None)

    if login_user is None:
        return None

    user: dict = {}
    user[login_user] = users.get(int(login_user))

    return user[login_user]


@babel.localeselector
def get_locale():
    """ Locale language

        Return:
            Best match to the language
    """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return locale

    locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ Locale language

        1.Find timezone parameter in URL parameters
        2.Find time zone from user settings
        3.Default to UTC

        Return:
            Timezone or Default UTC
    """
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tzone = pytz.timezone(timezone)
        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            tzone = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tzone = pytz.timezone(timezone)

    except exceptions.UnknownTimeZoneError:
        timezone = 'UTC'

    return timezone


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

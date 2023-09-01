#!/usr/bin/env python3
""" A flask app with a Babel object instance and localselector function."""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ A Babel configuration class."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages."""
    locale = request.args.get("locale")
    if locale is None:
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    return locale


def get_user():
    """ Method returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed."""
    userId = request.args.get("login_as")
    if userId:
        return users.get(int(userId))


@app.before_request
def before_request():
    """ Method to find a user if there are any."""
    g.user = get_user()


@app.route("/")
def home():
    """ Home page function."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/env python3
""" A basic flask app with a Babel object instance."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class config(object):
    """ A Babel configuration class."""
    LANGUAGES ={"en", "fr"}
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def home():
    """ Home page function."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/env python3
"""a flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
  """Babel config class"""
  LANGUAGES = ["en", "fr"]
  BABEL_DEFAULT_LOCALE = "en"
  BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    Determines the best match for supported languages.
    
    Checks for 'locale' parameter in the URL and uses it if valid.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Renders the index page, displaying a welcome message.
    """
    return render_template("4-index.html")

if __name__ == '__main__':
  app.run(debug=True)
  
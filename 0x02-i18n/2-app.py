#!/usr/bin/env python3
"""a flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
  """Babel config class"""
  LANGUAGES = ["en", "fr"]
  BABEL_DEFAULT_LOCALE = "en"
  BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
  """gets a locale timezone"""
  lang = request.accept_languages.best_match(app.config['LANGUAGES'])
  return lang

@app.route('/')
def index():
  """rendering a flask app"""
  return render_template('2-index.html')

if __name__ == '__main__':
  app.run(debug=True)
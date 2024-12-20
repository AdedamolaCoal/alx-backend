#!/usr/bin/env python3
"""a flask app"""

from flask import Flask, render_template, request, g
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
  """gets a locale timezone"""
  locale = request.args.get('locale')
  if locale in app.config['LANGUAGES']:
      return locale
  return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
  """rendering a flask app"""
  return render_template('2-index.html')

if __name__ == '__main__':
  app.run(debug=True)
  
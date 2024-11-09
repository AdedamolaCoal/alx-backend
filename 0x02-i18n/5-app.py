#!/usr/bin/env python3
"""
Flask app to demonstrate a simple login simulation with i18n support.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict

app = Flask(__name__)
babel = Babel(app)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configures the supported languages and default language for the app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

def get_user(login_as: Optional[int]) -> Optional[Dict]:
    """
    Retrieves a user dictionary from the mock users table.
    
    Args:
        login_as (Optional[int]): The user ID to look up.
    
    Returns:
        Optional[Dict]: The user dictionary if found, else None.
    """
    return users.get(login_as)

@app.before_request
def before_request():
    """
    Executed before each request. Sets g.user if a valid user is found.
    """
    login_as = request.args.get("login_as", type=int)
    g.user = get_user(login_as)

@babel.localeselector
def get_locale():
    """
    Selects the best match for supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Renders the index page, displaying a welcome message.
    """
    return render_template("5-index.html")

if __name__ == "__main__":
    app.run(debug=True)

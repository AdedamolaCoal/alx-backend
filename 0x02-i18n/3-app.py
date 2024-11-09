#!/usr/bin/env python3
"""Flask application for demonstrating i18n with Babel."""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

@app.route('/')
def home():
    """Render home page with translated strings."""
    return render_template('3-index.html')

@babel.localeselector
def get_locale():
    """Select locale based on the 'locale' URL parameter."""
    return request.args.get('locale', 'en')

if __name__ == "__main__":
    app.run(debug=True)

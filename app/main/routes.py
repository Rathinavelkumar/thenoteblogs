"""
Main site routes for TheNoteBlogs
"""

from flask import Blueprint, render_template, send_from_directory, current_app
import os
from . import main

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Renders the homepage."""
    return render_template('main/index.html', title='Home', carousel=True)

@main.route('/about')
def about():
    """Renders the About Us page."""
    return render_template('main/about.html', title='About Us', carousel=False)

@main.route('/terms')
def terms():
    """Renders the Terms of Use page."""
    return render_template('main/terms.html', title='Terms of Use', carousel=False)

@main.route('/privacy')
def privacy():
    """Renders the Privacy Policy page."""
    return render_template('main/privacy.html', title='Privacy Policy', contact_email='random@gmail.com', carousel=False)

@main.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(current_app.root_path, '..'), 'sitemap.xml', mimetype='application/xml')

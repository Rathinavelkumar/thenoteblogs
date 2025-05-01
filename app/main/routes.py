"""
Main site routes for TheNoteBlogs
"""

from flask import render_template
from . import main

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

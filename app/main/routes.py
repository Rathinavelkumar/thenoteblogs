from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('main/index.html', title='Home', carousel=True)

@main.route('/about')
def about():
    return render_template('main/about.html', title='About Us', carousel=False)

@main.route('/terms')
def terms():
    return render_template('main/terms.html', title='Terms of Use', carousel=False)

@main.route('/privacy')
def privacy():
    return render_template('main/privacy.html', title='Privacy Policy', contact_email='random@gmail.com', carousel=False)

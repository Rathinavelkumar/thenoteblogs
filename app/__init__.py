from flask import Flask
from flask_bootstrap import Bootstrap
import os

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'config.py'), silent=True)

    Bootstrap(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .stories import stories as stories_blueprint
    app.register_blueprint(stories_blueprint, url_prefix='/stories')

    from .movies import movies as movies_blueprint
    app.register_blueprint(movies_blueprint, url_prefix='/movies')

    return app

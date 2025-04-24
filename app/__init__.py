from flask import Flask
from app.model import db
from app.routes import bp as routes_bp
from app.config import Config

# Create function for app
def create_app():
    # create app instance
    app = Flask(__name__)

    # Set Config
    app.config.from_object(Config)

    # Initialize DB instance
    db.init_app(app)

    # Set Config
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(routes_bp)

    return app
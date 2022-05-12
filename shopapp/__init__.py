from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    register_blueprints(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app

def register_blueprints(app):
    from shopapp.recipes import recipes_blueprint
    from shopapp.users import users_blueprint

    app.register_blueprint(recipes_blueprint)
    app.register_blueprint(users_blueprint)

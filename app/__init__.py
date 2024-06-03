from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app.config import config

import os

ma = Marshmallow()
db = SQLAlchemy()


def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
      
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DEV_DATABASE_URI')

    ma.init_app(app)
    f.init_app(app)
    db.init_app(app)

    from app.resources import auth
    app.register_blueprint(auth, url_prefix='/api/v1/auth')
  
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app

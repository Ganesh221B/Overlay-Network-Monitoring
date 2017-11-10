import os
from flask import Flask, request

import config as Config
from .common import Response
from .common import constants as COMMON_CONSTANTS
from .frontend import frontend
from .models import User
from .extensions import db, login_manager, csrf


# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None, blueprints=None):
   """Create a Flask app."""

   if app_name is None:
     app_name = Config.DefaultConfig.PROJECT
   if blueprints is None:
     blueprints = DEFAULT_BLUEPRINTS

   app = Flask(app_name, instance_path=COMMON_CONSTANTS.INSTANCE_FOLDER_PATH, instance_relative_config=True)
   configure_app(app, config)
   configure_hook(app)
   configure_extensions(app)
   configure_logging(app)
   configure_error_handlers(app)
   
   return app
   
   def configure_app(app, config=None):
   

   # http://flask.pocoo.org/docs/api/#configuration
   app.config.from_object(Config.DefaultConfig)

   if config:
     app.config.from_object(config)
     return

   
   application_mode = os.getenv('APPLICATION_MODE','LOCAL')
   app.config.from_object(Config.get_config(application_mode))

def configure_extensions(app):
   
   db.init_app(app)
   
 

   @login_manager.user_loader
   def load_user(id):
      return User.query.get(id)

   login_manager.setup_app(app)

   @login_manager.unauthorized_handler
   def unauthorized(msg=None):
       
       return Response.make_error_resp(msg="You're not authorized!", code=401)
     
     
   # flask-wtf
   csrf.init_app(app)
import os
from common.constants import INSTANCE_FOLDER_PATH

class BaseConfig(object):

   PROJECT = "app"

  
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

   DEBUG = False
   TESTING = False

   ADMINS = ['shravyanuka09@gmail.com']

  
   SECRET_KEY = 'secret key'
   
 class DefaultConfig(BaseConfig):

   DEBUG = True

   SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
   
   SECRET_KEY = 'development key'
   
   class LocalConfig(DefaultConfig):
   pass

class StagingConfig(DefaultConfig):
    
    pass

class ProdConfig(DefaultConfig):
    pass

def get_config(MODE):
   SWITCH = {
      'LOCAL'     : LocalConfig,
      'STAGING'   : StagingConfig,
      'PRODUCTION': ProdConfig
   }
   return SWITCH[MODE]
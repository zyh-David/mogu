from . import Config
class DevConfig(Config):
  """开发模式下的配置"""
  DEBUG = True
  SQLALCHEMY_ECHO = True
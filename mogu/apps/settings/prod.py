from . import Config
class ProdConfig(Config):
    """生产模式下的配置"""
    DEBUG = False
    LOG_LEVEL = "INFO"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
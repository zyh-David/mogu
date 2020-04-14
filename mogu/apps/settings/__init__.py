import os
import sys
from redis import Redis
from apps.utils.helper import get_redis_connection
class Config(object):
	"""项目公共配送至"""
	# 把主应用目录设置为 默认导包路径
	BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) # apps
	sys.path.insert(0, BASE_DIR )
	# 把蓝图存储设置默认导包路径
	sys.path.insert(0, os.path.join(BASE_DIR, "modules") )

	# 调试模式
	DEBUG = True

	# 设置密钥，可以通过 base64.b64encode(os.urandom(48)) 来生成一个指定长度的随机字符串
	SECRET_KEY = "T1vEjTCjkGon5vU8C6Xq3ujNSQgHQje"

	# 配置日志
	LOG_LEVEL = "DEBUG"
	LOG_FILE_PATH = os.path.join( os.path.dirname( BASE_DIR ), "logs/mogu.log" )
	LOG_FILE_SIZE = 500 * 1024* 1024
	LOG_FILE_NUMBER = 10

	# 数据库的配置信息
	SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/moguapp?charset=utf8"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = False

	# redis配置
	REDIS = {
		'default': {
			'host': '127.0.0.1',  # 项目上线以后，这个地址就会被替换成真实IP地址，mysql也是
			'port': 6379,
			'db': 0
		},
		'session': {
			'host': '127.0.0.1',  # 项目上线以后，这个地址就会被替换成真实IP地址，mysql也是
			'port': 6379,
			'db': 1
		}
	}


	# session 配置
	SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
	SESSION_USE_SIGNER = True  # session_id 进行加密签名处理
	SESSION_REDIS = get_redis_connection( REDIS.get("session") )
	PERMANENT_SESSION_LIFETIME = 24 * 60 * 60  # session 的有效期，单位是秒
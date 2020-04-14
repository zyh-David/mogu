from apps import db
from utils.models import BaseModel

class SiteConfig(BaseModel, db.Model):
	"""站点配置"""
	__tablename__ = "mogu_site_config"
	id    = db.Column( db.Integer, primary_key=True,comment="ID" )
	title = db.Column( db.String(80),comment="提示文本" )
	name  = db.Column( db.String(500), nullable=True, comment="变量名")
	value = db.Column( db.String(500), nullable=True, comment="变量值")
	dtype = db.Column( db.Enum( "text", "image", "link", "video" ), default="text", comment="变量类型" )

	def __repr__(self):
		return "%s[%s]=%s" % (self.title,self.name,self.value)

class Nav(BaseModel, db.Model):
	"""导航菜单"""
	__tablename__ = "mogu_nav"
	id = db.Column( db.Integer, primary_key=True, comment="ID" )
	name = db.Column( db.String(80), comment="导航名称" )
	link = db.Column( db.String(164), nullable=True, comment="导航链接")
	parent_id = db.Column(db.Integer, db.ForeignKey('mogu_nav.id'),comment="父导航ID")
	# 自关联
	parent = db.relationship('Nav', uselist=False, remote_side=[id], backref=db.backref('children', uselist=True) ) # 父导航

	def __repr__(self):
		return "%s" % (self.name)

class Banner(BaseModel, db.Model):
	"""轮播广告"""
	__tablename__ = "mogu_banner"
	id = db.Column( db.Integer, primary_key=True,comment="ID")
	title = db.Column( db.String(80),comment="轮播标题" )
	link  = db.Column( db.String(164), nullable=True, comment="广告链接")
	image_url = db.Column(db.String(256), nullable=True, comment="图片路径")

	def __repr__(self):
		return "%s" % (self.title)
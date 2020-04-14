from apps import db
from apps.utils.models import BaseModel

class NewsCategory(BaseModel, db.Model):
    """文章分类"""
    __tablename__ = "mogu_news_category"
    id = db.Column( db.Integer, primary_key=True, comment="ID" )
    name = db.Column(db.String(64), nullable=True, comment="分类名称")
    news_list = db.relationship('News', backref='category', lazy='dynamic')

    def __repr__(self):
        return "%s" % (self.name)

class News(BaseModel, db.Model):
    """文章信息"""
    __tablename__ = "mogu_news"
    id = db.Column( db.Integer, primary_key=True,comment="ID" )
    title = db.Column(db.String(256), nullable=False,comment="文章标题" )
    descript = db.Column(db.String(512), nullable=False,comment="文章摘要" )
    content = db.Column(db.Text, nullable=False,comment="文章内容" )
    read_count = db.Column(db.Integer, default=0,comment="浏览量" )
    image_url = db.Column(db.String(256), default='',comment="封面图片")
    author = db.Column(db.String(64),comment="作者" )
    is_recommend = db.Column( db.Boolean, default=False, comment="是否推荐到首页" )
    category_id = db.Column(db.Integer, db.ForeignKey("mogu_news_category.id"),comment="分类ID")

    def __repr__(self):
        return "%s" % (self.title)
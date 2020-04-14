# 数据模型

## 模型分析

```
公共模块
	导航菜单
        id
        name
        parent_id
        link
        sort
        is_show
        is_deleted
        created_time
        updated_time

    轮播广告
        id
        title
        image_url
        link
        sort
        is_show
        is_deleted
        created_time
        updated_time

    站点配置
        id
        title
        name
        value
        dtype
        sort
        is_show
        is_deleted
        created_time
        updated_time
        
商品模块
    商品分类
        id
        name
        sort
        is_show
        is_deleted
        created_time
        updated_time

	商品信息
        id
        title
        catetory_id
        image_url
        is_recommend   是否推荐到首页
        description
        effect
        sort
        is_show
        is_deleted
        created_time
        updated_time

    商品图片
        
	商品类型
		
	商品属性
        
	参数选项数值
		
	商品参数数值
	
	商品库存表
		
文章模块
	文章分类
        id
        name
        sort
        is_show
        is_deleted
        created_time
        updated_time

    文章资讯
        id
        title
        read_count   阅读量
        descript
        content
        sort
        is_show
        is_deleted
        created_time
        updated_time
```



站点配置信息的分析[开发人员]

| id   | title        | name      | value           | dtype |
| ---- | ------------ | --------- | --------------- | ----- |
| 1    | 站点logo图片 | logo      | images/logo.png | image |
| 2    | 版权信息     | copyright | 蘑菇街@版权所有 | text  |
|      |              |           |                 |       |



#### 数据模型之间的关系

![1559618857957](assets/1559618857957.png)



### 构建模型

我们这里有8个数据模型，这些数据模型都存在一些公共的字段，所以我们可以封装一个公共模型BaseModel出来。而且8个模型，分别属于公共模块[站点配置，轮播广告和导航菜单]，文章模块[文章分类和文章信息]和商品模块[商品分类，商品SPU和商品图片]

注意,因为商品的图片是显示在 详情页的信息,所以我们可以后续处理.暂时先不创建这个商品图片模型.



utils/models.py，代码：

```python
from apps import db
from datetime import datetime
import copy
class BaseModel(object):
	sort = db.Column(db.Integer, default=None, nullable=True, comment="排序")
	is_deleted = db.Column(db.Boolean, default=False, comment="逻辑删除")
	is_show = db.Column(db.Boolean, default=True, comment="是否显示")
	created_time = db.Column(db.DateTime, default=datetime.now, comment="添加时间")
	updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

	# 模型.__to_dict__(["id","mame","age"])
	def __to_dict__(self,fields=None):
		"""把模型对象转换成字典"""
		self.created_time = self.created_time.strftime("%Y-%m-%d %H:%M:%S")
		self.updated_time = self.updated_time.strftime("%Y-%m-%d %H:%M:%S")

		data = self.__dict__
		data_dict = copy.deepcopy(data)

		# 从字典中移除掉表示外键关系的属性
		if "_sa_instance_state" in data_dict:
			data_dict.pop("_sa_instance_state")

		# 如果不指定fields,则默认返回模型的所有数据
		if fields is None:
			return data_dict

		# fields不是None, 则根据fields来决定要返回哪些字段数据
		result = {}
		for key,value in data_dict.items():
			if key in fields:
				result[key] = value

		return result
```



modules/home/models.py，公共模块的api模型代码：

```python
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
```



modules/news/models.py，文章模块的api模型代码：

```python
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
```

modules/goods/api.py，商品模块的api模型代码：

```python
from apps import db
from utils.models import BaseModel

class GoodsCategory(BaseModel, db.Model):
    """商品分类"""
    __tablename__ = "mogu_goods_category"
    id = db.Column( db.Integer, primary_key=True,comment="ID" )
    name = db.Column(db.String(64), nullable=True,comment="分类名称")
    goods_list = db.relationship('GoodsSPU', backref='category', lazy='dynamic')

    def __repr__(self):
        return "%s" % (self.name)

class GoodsSPU(BaseModel, db.Model):
    """商品SPU"""
    __tablename__ = "mogu_goods_spu"
    id = db.Column( db.Integer, primary_key=True,comment="ID" )
    title = db.Column(db.String(256), nullable=False,comment="商品标题" )
    is_recommend = db.Column( db.Boolean, default=False, comment="是否推荐到首页" )
    descript = db.Column(db.String(512), nullable=False,comment="商品描述" )
    effect = db.Column(db.Text, nullable=False,comment="产品效果" )
    image_url = db.Column(db.String(256), default='',comment="封面图片")
    category_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_category.id"),comment="分类ID")
```

```
spu是描述商品的抽象单位,表示一个款式或者一个系列,不是真实单位
```

#### 数据迁移

把所有需要进行迁移的模型导入到manage.py中进行注册

```python
from apps import init_app

app = init_app("dev")


# 引入modules目录下面的api接口
from home import api

# 引入modules目录下面的模型
from home.models import SiteConfig,Nav,Banner
from goods.models import GoodsCategory,GoodsSPU
from news.models import NewsCategory,News

if __name__ == '__main__':
    app.manager.run()
```



使用启动文件的数据迁移命令

```shell
python manage.py db init
python manage.py db migrate -m "init models"
python manage.py db upgrade
```
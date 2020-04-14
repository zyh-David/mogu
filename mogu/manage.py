# encoding=utf-8

from apps import init_app,db

app = init_app("dev")

# 引入modules目录下面的api接口
from home import api
from goods import api
from news import api

# 引入modules目录下面的模型
from home.models import SiteConfig,Nav,Banner
from goods.models import GoodsCategory,GoodsSPU
from news.models import NewsCategory,News

# 把模型注册到admin站点后台
from flask_admin.contrib.sqla import ModelView
class MyModelView(ModelView):
    pass
app.admin.add_view( MyModelView(SiteConfig,db.session,name="站点配置") )
app.admin.add_view( MyModelView(Nav,db.session,name="导航菜单") )
app.admin.add_view( MyModelView(Banner,db.session,name="轮播广告") )
app.admin.add_view( MyModelView(GoodsCategory,db.session,name="商品分类") )
app.admin.add_view( MyModelView(GoodsSPU,db.session,name="商品SPU") )

if __name__ == '__main__':
    app.manager.run()
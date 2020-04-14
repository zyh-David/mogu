# 商品属性展示

## 后端实现商品属性API接口

### 创建商品属性相关的模型

![1559813158673](assets/1559813158673.png)

```python
from apps import db
from apps.utils.models import BaseModel

class GoodsCategory(BaseModel, db.Model):
    """商品分类"""
    __tablename__ = "mogu_goods_category"
    id = db.Column( db.Integer, primary_key=True,comment="ID" )
    name = db.Column(db.String(64), nullable=True,comment="分类名称")
    goods_list = db.relationship('SPU', backref='category', lazy='dynamic')

class SPU(BaseModel, db.Model):
    """商品SPU"""
    __tablename__ = "mogu_goods"
    id = db.Column( db.Integer, primary_key=True,comment="ID" )
    type_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_type.id"), comment="类型ID")
    title = db.Column(db.String(256), nullable=False,comment="商品标题" )
    is_recommend = db.Column( db.Boolean, default=False, comment="是否推荐到首页" )
    descript = db.Column(db.String(512), nullable=False,comment="商品描述" )
    effect = db.Column(db.Text, nullable=False,comment="穿着效果" )
    image_url = db.Column(db.String(256), default='',comment="封面图片")
    category_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_category.id"),comment="分类ID")
    sale_total = db.Column(db.Integer, default=0, comment="系列产品的总销量")

class GoodsImage(BaseModel, db.Model):
    """商品图片"""
    __tablename__ = "mogu_goods_image"
    id = db.Column( db.Integer, primary_key=True,comment="ID" )
    image_url = db.Column(db.String(256), default='',comment="封面图片")
    goods_id = db.Column(db.Integer, db.ForeignKey("mogu_goods.id"),comment="商品ID")
    sku_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_sku.id"), default=0, nullable=True, comment="SKU_ID")

class GoodsType(BaseModel, db.Model):
    """商品类型"""
    __tablename__ = "mogu_goods_type"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    name = db.Column(db.String(64), nullable=True, comment="类型名称")
    goods_spu_list = db.relationship('SPU', backref='goods_type', lazy='dynamic')
    attr_list = db.relationship('GoodsAttribute', backref='goods_type', lazy='dynamic')

class GoodsSKU(BaseModel, db.Model):
    """商品SKU基本信息"""
    __tablename__ = "mogu_goods_sku"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    name = db.Column(db.String(500), nullable=True, comment="SKU商品名称")
    spu_id = db.Column(db.Integer, db.ForeignKey("mogu_goods.id"), comment="SPU商品ID")
    sale = db.Column(db.Integer, comment="单品销量")
    number = db.Column(db.Integer, comment="库存量")
    price = db.Column(db.Numeric(8, 2), comment="商品进货价")
    sale_price = db.Column(db.Numeric(8, 2), comment="商品销售价")
    attr_list = db.relationship('GoodsSKUAttribute', backref='goods_sku', lazy='dynamic')
    img_list = db.relationship('GoodsImage', backref='sku_image', lazy='dynamic')

class GoodsAttribute(BaseModel, db.Model):
    """商品属性"""
    __tablename__ = "mogu_goods_attribute"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    name = db.Column(db.String(64), nullable=True, comment="属性名称")
    type_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_type.id"), comment="类型ID")
    value_type = db.Column(db.Enum("唯一值", "单选值"), default="唯一值")
    input_type = db.Column(db.Enum("手动录入", "下拉列表"), default="手动录入")
    option_list = db.relationship('GoodsAttributeOption', backref='option_arrtibute', lazy='dynamic')
    sku_list = db.relationship('GoodsSKUAttribute', backref='goods_attribute', lazy='dynamic')

class GoodsAttributeOption(BaseModel, db.Model):
    """商品属性值选项"""
    __tablename__ = "mogu_goods_attribute_option"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    attr_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_attribute.id"), comment="属性ID")
    option = db.Column(db.String(64), nullable=True, comment="选项值")

class GoodsSKUAttribute(BaseModel, db.Model):
    """SKU商品属性值"""
    __tablename__ = "mogu_goods_sku_attribute"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    sku_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_sku.id"), comment="SKU_ID")
    attr_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_attribute.id"), comment="属性ID")
    value = db.Column(db.String(640), nullable=True, comment="属性值")
    option_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_attribute_option.id"), default=0, nullable=True, comment="属性ID")

```

通过git上传到服务器，在服务器中执行数据迁移

```bash
python manage.py db migrate -m '新增商品sku和商品属性相关的模型'
python manage.py db upgrade
```



### 实现商品属性的API接口

添加测试数据

```sql
# 添加商品类型
INSERT INTO `mogu_goods_type` (`name`,`is_deleted`,`is_show`) values ('衣服',0,1),('手机',0,1),('笔记本',0,1);

# 给所有商品指定商品类型为衣服
update mogu_goods set type_id = 1; 

# 添加商品SKU
INSERT INTO `mogu_goods_sku` (`spu_id`,`sale`,`number`,`price`,`is_deleted`,`is_show`) values (1,100,100,100,0,1),(1,100,100,100,0,1),(2,100,100,100,0,1),(2,100,100,100,0,1),(2,100,100,100,0,1),(2,100,100,100,0,1),(3,100,100,100,0,1),(4,100,100,100,0,1),(4,100,100,100,0,1),(4,100,100,100,0,1),(5,100,100,100,0,1),(5,100,100,100,0,1);

# 在sku表中设置销售价=进货价*1.22
UPDATE `mogu_goods_sku` SET sale_price=price*1.22; 

# 添加商品属性
INSERT INTO `mogu_goods_attribute` (`type_id`,`name`,`value_type`,`is_deleted`,`is_show`) values (1,'尺码','单选值',0,1),(2,'腰型','单选值',0,1),(1,'袖长','单选值',0,1),(1,'颜色','单选值',0,1),(1,'领型','单选值',0,1);

# 添加商品属性值选项
INSERT INTO `mogu_goods_attribute_option` (`attr_id`,`option`,`is_deleted`,`is_show`) values (1,'S',0,1),(1,'L',0,1),(1,'M',0,1),(1,'XL',0,1),(1,'XXL',0,1),(1,'XXXL',0,1),(2,'高腰',0,1),(2,'中腰',0,1),(2,'低腰',0,1),(3,'短袖',0,1),(3,'长袖',0,1),(3,'中长袖',0,1),(3,'无袖',0,1),(4,'纯色',0,1),(4,'黑紫色',0,1),(4,'白色',0,1),(4,'天蓝色',0,1),(4,'粉色',0,1),(5,'圆领',0,1),(5,'无领',0,1),(5,'V领',0,1);


# 添加具体商品的属性和属性值关系
INSERT INTO `mogu_goods_sku_attribute` (`attr_id`,`value`,`sku_id`,`is_deleted`,`is_show`) values (1,1,1,0,1),(2,7,1,0,1),(3,13,1,0,1),(4,14,1,0,1),(5,21,1,0,1),(1,3,2,0,1),(2,7,2,0,1),(3,13,2,0,1),(4,15,2,0,1),(5,21,2,0,1);

```



### 对外提供API接口

因为我们需要提供商品价格给客户端，所以价格字段本身是Decimal类型，因此我们需要修改调整BaseModel类下面的工具方法`__to__dict__`，调整如下：

```python
from apps import db
from datetime import datetime
import copy
from decimal import Decimal
class BaseModel(object):
    """模型基类"""
    created_time = db.Column( db.DateTime, default=datetime.now, comment="添加时间" )
    updated_time = db.Column( db.DateTime, default=datetime.now, onupdate=datetime.now,comment="更新时间" )
    sort        = db.Column( db.Integer, default=0,comment="排序" )
    is_deleted  = db.Column( db.Boolean, default=False,comment="逻辑删除" )
    is_show     = db.Column( db.Boolean, default=True,comment="是否显示" )

    def __to_dict__(self,fields=None):
        """把模型转换成字典"""
        try:
            self.create_time = self.create_time.strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass
        try:
            self.update_time = self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        except:
            pass

        data = self.__dict__
        if fields is None:
            data_dict = copy.deepcopy(data)
            if "_sa_instance_state" in data_dict:
                data_dict.pop("_sa_instance_state")

        else:
            data_dict = {}
            for key,value in data.items():
                if key in fields:
                    data_dict[key] = value

        # 兼容处理 Decimal类型数据无法进行json序列化
        for key,value in data_dict.items():
            if isinstance(value, Decimal):
                data_dict[key] = float(value)

        return data_dict
```



查询当前页面spu商品对应的所有SKU商品。

```python
@jsonrpc_v1.method("Goods.detail_sku_goods(spu_id=Number)")
def detail_sku_goods(spu_id):
	"""获取详情页中的spu_id对应的SKU商品"""
	sku_list = GoodsSKU.query.filter(
		GoodsSKU.spu_id == spu_id,
		GoodsSKU.is_show == True,
		GoodsSKU.is_deleted == False
	).order_by(
		db.desc(GoodsSKU.sort),
		db.desc(GoodsSKU.id)
	).all()

	data = []
	for sku in sku_list:
		sku_dict = sku.__to_dict__(["name","sale","number","sale_price"])
		data.append(sku_dict)

	return data
```





### APP获取商品属性API

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-蘑菇网-你的专业导购</title>
  <meta name="Keywords" content="换季,新品" />
  <meta name="Description" content="换季,换季,换季,换季,换季,换季,换季,换季,换季" />
  <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
  <!-- Mobile Devices Support @begin -->
  <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
  <!-- Mobile Devices Support @end -->
  <link href="../css/index.css" rel="stylesheet" />
  <link href="../css/common.css" rel="stylesheet" />
  <link href="../css/swiper.min.css" rel="stylesheet" />
  <script src="../script/jquery-1.9.1.min.js"></script>
  <script src="../script/main.js"></script>
  <script src="../script/jquery.rotate.min.js"></script>
  <script src="../script/swiper.min.js"></script>
</head>
<body>
<div class="main" id="app">
  <!--头部-->
<div class="header" id="bktop">
  <div class="logo"><a href=""><img :src="'../'+siteconfig.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
          <ul class="xla">
              <li v-for="top in nav_list">
                  <a class="dianj dj1" :href="top.link"><font>{{top.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
                  <div class="zilan">
                      <a :href="son.link" v-for="son in top.children_list">{{son.name}}</a>
                  </div>
              </li>
          </ul>
      </div>
      <div class="clearBoth"></div>
  </div>
  <!--产品信息-->
  <div class="newsban"><a style="color:#ccc" href="">首页</a> > <a style="color:#ccc" href="">换季新品</a> > {{goods.title}} </div>
  <div id="main">
    <div class="home-device">
      <a class="arrow-left" href="#"></a>
      <a class="arrow-right" href="#"></a>
      <div class="swiper-main">
        <div class="swiper-container swiper1">
          <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="item in goods_image"><img :src="item.image_url" width="100%"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="dian"><div class="pagination pagination1"></div></div>
  </div>
  <div class="newbt2" v-if="sku_goods.sale_price">{{sku_goods.name}} <span class="goods_price">￥{{sku_goods.sale_price.toFixed(2)}}</span></div>
  <ul class="sku_list">
      <li @click="change_sku_id(sku.id)" v-for="sku in sku_list" v-if="sku">{{sku.name}}</li>
  </ul>
  <div class="about">
    <div class="content2">
      <!-- start -->
      <div class="page-btn">
        <span class="swiper-pagination-active">商品详情</span>
        <span>商品参数</span>
        <span>同类热门</span>
      </div>
      <div class="swiper-container swiper2">
        <div class="swiper-wrapper" style="min-height: 500px;">
          <div class="swiper-slide product-content">
            <p class="image-list-title"><span>商品描述</span></p>
            <p class="product-desc">{{goods.descript}}</p>
            <p class="image-list-title"><span>穿着效果</span></p>
            <div class="product-desc" style="color: #fff;min-height: 100px;" v-html="goods.effect"></div>
          </div>
          <div class="swiper-slide product-param">
            <table class="parameter-table">
                <tr v-for="value,key in sku_goods_attr">
                    <td>{{key}}: {{value}}</td>
                </tr>
            </table>
          </div>
          <div class="swiper-slide">
            <div class="case_list">
              <div class="case_list_body case_list_body2 case_list_body3">
                <ul>
                  <li :class="key%2==0?'yyu':'casela'" v-for="item,key in hot_goods">
                      <a href="">
                        <div class="case_list_body_pic">
                          <img :src="'../'+item.image_url">
                        </div>
                      </a>
                      <div class="case_list_info">
                        <p class="cast_list_tit"><a href="">{{item.title}}</a></p>
                      </div>
                  </li>
                  <div class="clearBoth"></div>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!--底部-->
  <div class="bottom">
      <div class="bottom-top">
          <div class="linker">
              <div class="liuy">
                  <a href="">
                      <div class="tubiao"><img src="../image/liuy.gif" /></div>
                      <div class="wenzi">在线留言</div>
                      <div class="clearBoth"></div>
                  </a>
              </div>
              <div class="clearBoth"></div>
          </div>
      </div>
      <div class="bottom-bot">{{siteconfig.copyright}}</div>
  </div>
</div>
<script src="../script/vue.js"></script>
<script src="../script/axios.js"></script>
<script src="../script/tools.js"></script>
<script src="../script/settings.js"></script>
<script>
    var vm = new Vue({
      el:"#app",
      data:{
        siteconfig:{},
        nav_list:[
          {
            children_list:[],
          },{
            children_list:[],
          },{
            children_list:[],
          },
        ],
        goods:{},      // spu商品信息
        sku_goods:{},  // sku商品信息
        goods_image:[],
        hot_goods:[],
        sku_list:[],
        spu_id: 1,
        sku_id: 2,
        category: 0,
        sku_goods_attr:{}
      },
      watch:{
        sku_id(){
          // 监听sku_id的变化
          for(key in this.sku_list){
            if(this.sku_list[key].id == this.sku_id){
              this.sku_goods = this.sku_list[key];
            }
          }
          this.get_attr_by_sku_id();
        },
      },
      created(){
          this.get_site_config();
          this.get_nav_list();
          this.get_goods();
          this.get_goods_image();
          this.get_sku_by_spu_id();
      },
      methods:{
        change_sku_id(sku_id){
          // 切换不同的SKU商品ID
          this.sku_id = sku_id;
        },
        get_site_config(){
          // 獲取站點配置的api接口
          rpc(settings.API, "Common.siteconfig", {}, (data)=>{
            this.siteconfig = data;
          });
        },
        get_nav_list(){
          // 獲取導航菜單的api接口
          rpc(settings.API, "Common.nav", {}, (data)=>{
            this.nav_list = data;
          });
        },
        get_goods(){
          //. 获取商品详情的基本信息
          rpc(settings.API, "Goods.detail_goods", {id:this.spu_id}, (data)=>{
            this.goods = data;
            // 获取同类热门商品
            this.category = this.goods.category_id;
            this.get_hot_goods();
          });
        },
        get_goods_image(){
          // 获取当前商品相关的图片信息
          rpc(settings.API, "Goods.detail_goods_image", {id:this.spu_id}, (data)=>{
            this.goods_image = data;
          });
        },
        get_hot_goods(){
          // 获取当前商品的同类热门商品
          rpc(settings.API, "Goods.hot_goods", {goods_id:this.spu_id,category:this.category}, (data)=>{
            this.hot_goods = data;
          });
        },
        get_sku_by_spu_id(){
          // 通过SPU来获取所有的SKU库存商品
          rpc(settings.API, "Goods.detail_sku_goods", {spu_id:this.spu_id}, (data)=>{
            let result = []
            for( let key in data ){
              if(key==0){
                // 默认让当前页面显示列表第一个成员的信息
                this.sku_goods = data[key];
              }
              result[data[key].id] = data[key];
            }
            this.sku_list = result;
            this.get_attr_by_sku_id();
          });
        },
        get_attr_by_sku_id(){
          // 根据sku商品的id获取当前商品具体的商品属性
          rpc(settings.API, "Goods.sku_goods_attr",  {sku_id:this.sku_goods.id}, (data)=>{
            // 对数据进行重构
            this.sku_goods_attr = data;
          });
        }
      }
    });

  $(function(){
        // 商品图片
       var swiper = new Swiper('.swiper1', {
         pagination : '.pagination1',
         loop: true,
         paginationClickable: true,
         autoplay : 5000,
         grabCursor: true,
         autoHeight: true,
       });

       // 商品详情
       var swiper2 = new Swiper('.swiper2', {
         autoHeight: true,
         onSlideChangeStart: function(swiper){
           $('.page-btn span').eq(swiper.activeIndex).addClass('swiper-pagination-active').siblings().removeClass('swiper-pagination-active');
         }
       });

       // 按钮设置
       $('.page-btn span').click(function(){
         $(this).addClass('swiper-pagination-active').siblings().removeClass('swiper-pagination-active');
         swiper2.slideTo( $(this).index(), 500, false);
       });
  })
</script>
</body>
</html>
```





在商品详情页面中，展示当前sku商品对应的价格！

```python
在商品标题处增加价格内容的显示：
  <div class="newbt2">{{goods.title}} <span class="goods_price">￥40.00</span></div>
  <ul class="sku_list">
    <li v-for="sku in sku_list"><span>{{sku.name}}</span></li>
  </ul>
  
css样式：
.goods_price{float: right; font-size: 24px;color: #f55;margin-right: 2em;}
.sku_list{ color: #FFF; margin: 20px 20px 20px 36px; line-height: 32px; text-decoration: underline;}
```

把数据库中现有的SKU的商品标题进行修改：

```python
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-1' where id=1;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-2' where id=2;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-3' where id=3;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-4' where id=4;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-5' where id=5;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-6' where id=6;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-7' where id=7;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-8' where id=8;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-9' where id=9;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-10' where id=10;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-11' where id=11;
update `mogu_goods_sku` set name='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-12' where id=12;
```



在客户端中根据当前的SPU商品ID获取所有的SKU商品属性

goods/api.py，代码：

```python
from .models import GoodsSKUAttribute,GoodsAttributeOption
@jsonrpc_v1.method("Goods.sku_goods_attr(sku_id=Number)")
def sku_goods_attr(sku_id):
	"""根据sku_id获取商品属性"""
	attr_list = GoodsSKUAttribute.query.filter(GoodsSKUAttribute.sku_id==sku_id).all()
	attr_dict = {}
	for item in attr_list:
		arrt_name = item.goods_attribute.name
		value     = GoodsAttributeOption.query.get(item.value).option
		attr_dict[arrt_name] = value

	return attr_dict
```



### APP获取商品属性API

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-蘑菇网-你的专业导购</title>
  <meta name="Keywords" content="换季,新品" />
  <meta name="Description" content="换季,换季,换季,换季,换季,换季,换季,换季,换季" />
  <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
  <!-- Mobile Devices Support @begin -->
  <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
  <!-- Mobile Devices Support @end -->
  <link href="../css/index.css" rel="stylesheet" />
  <link href="../css/common.css" rel="stylesheet" />
  <link href="../css/swiper.min.css" rel="stylesheet" />
  <script src="../script/jquery-1.9.1.min.js"></script>
  <script src="../script/main.js"></script>
  <script src="../script/jquery.rotate.min.js"></script>
  <script src="../script/swiper.min.js"></script>
</head>
<body>
<div class="main" id="app">
  <!--头部-->
<div class="header" id="bktop">
  <div class="logo"><a href=""><img :src="'../'+siteconfig.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
          <ul class="xla">
              <li v-for="top in nav_list">
                  <a class="dianj dj1" :href="top.link"><font>{{top.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
                  <div class="zilan">
                      <a :href="son.link" v-for="son in top.children_list">{{son.name}}</a>
                  </div>
              </li>
          </ul>
      </div>
      <div class="clearBoth"></div>
  </div>
  <!--产品信息-->
  <div class="newsban"><a style="color:#ccc" href="">首页</a> > <a style="color:#ccc" href="">换季新品</a> > {{goods.title}} </div>
  <div id="main">
    <div class="home-device">
      <a class="arrow-left" href="#"></a>
      <a class="arrow-right" href="#"></a>
      <div class="swiper-main">
        <div class="swiper-container swiper1">
          <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="item in goods_image"><img :src="item.image_url" width="100%"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="dian"><div class="pagination pagination1"></div></div>
  </div>
  <div class="newbt2" v-if="sku_goods.sale_price">{{sku_goods.name}} <span class="goods_price">￥{{sku_goods.sale_price.toFixed(2)}}</span></div>
  <ul class="sku_list">
      <li v-for="sku in sku_list" v-if="sku">{{sku.name}}</li>
  </ul>
  <div class="about">
    <div class="content2">
      <!-- start -->
      <div class="page-btn">
        <span class="swiper-pagination-active">商品详情</span>
        <span>商品参数</span>
        <span>同类热门</span>
      </div>
      <div class="swiper-container swiper2">
        <div class="swiper-wrapper" style="min-height: 500px;">
          <div class="swiper-slide product-content">
            <p class="image-list-title"><span>商品描述</span></p>
            <p class="product-desc">{{goods.descript}}</p>
            <p class="image-list-title"><span>穿着效果</span></p>
            <div class="product-desc" style="color: #fff;min-height: 100px;" v-html="goods.effect"></div>
          </div>
          <div class="swiper-slide product-param">
            <table class="parameter-table">
                <tr v-for="value,key in sku_goods_attr">
                    <td>{{key}}: {{value}}</td>
                </tr>
            </table>
          </div>
          <div class="swiper-slide">
            <div class="case_list">
              <div class="case_list_body case_list_body2 case_list_body3">
                <ul>
                  <li :class="key%2==0?'yyu':'casela'" v-for="item,key in hot_goods">
                      <a href="">
                        <div class="case_list_body_pic">
                          <img :src="'../'+item.image_url">
                        </div>
                      </a>
                      <div class="case_list_info">
                        <p class="cast_list_tit"><a href="">{{item.title}}</a></p>
                      </div>
                  </li>
                  <div class="clearBoth"></div>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!--底部-->
  <div class="bottom">
      <div class="bottom-top">
          <div class="linker">
              <div class="liuy">
                  <a href="">
                      <div class="tubiao"><img src="../image/liuy.gif" /></div>
                      <div class="wenzi">在线留言</div>
                      <div class="clearBoth"></div>
                  </a>
              </div>
              <div class="clearBoth"></div>
          </div>
      </div>
      <div class="bottom-bot">{{siteconfig.copyright}}</div>
  </div>
</div>
<script src="../script/vue.js"></script>
<script src="../script/axios.js"></script>
<script src="../script/tools.js"></script>
<script src="../script/settings.js"></script>
<script>
    var vm = new Vue({
      el:"#app",
      data:{
        siteconfig:{},
        nav_list:[
          {
            children_list:[],
          },{
            children_list:[],
          },{
            children_list:[],
          },
        ],
        goods:{},      // spu商品信息
        sku_goods:{},  // sku商品信息
        goods_image:[],
        hot_goods:[],
        sku_list:[],
        id: 1,
        sku_id: 2,
        category: 0,
        sku_goods_attr:{}
      },
      created(){
          this.get_site_config();
          this.get_nav_list();
          this.get_goods();
          this.get_goods_image();
          this.get_sku_by_spu_id();
      },
      methods:{
        get_site_config(){
          // 獲取站點配置的api接口
          rpc(settings.API, "Common.siteconfig", {}, (data)=>{
            this.siteconfig = data;
          });
        },
        get_nav_list(){
          // 獲取導航菜單的api接口
          rpc(settings.API, "Common.nav", {}, (data)=>{
            this.nav_list = data;
          });
        },
        get_goods(){
          //. 获取商品详情的基本信息
          rpc(settings.API, "Goods.detail_goods", {id:this.id}, (data)=>{
            this.goods = data;
            // 获取同类热门商品
            this.category = this.goods.category_id;
            this.get_hot_goods();
          });
        },
        get_goods_image(){
          // 获取当前商品相关的图片信息
          rpc(settings.API, "Goods.detail_goods_image", {id:this.id}, (data)=>{
            this.goods_image = data;
          });
        },
        get_hot_goods(){
          // 获取当前商品的同类热门商品
          rpc(settings.API, "Goods.hot_goods", {goods_id:this.id,category:this.category}, (data)=>{
            this.hot_goods = data;
          });
        },
        get_sku_by_spu_id(){
          // 通过SPU来获取所有的SKU库存商品
          rpc(settings.API, "Goods.detail_sku_goods", {spu_id:this.id}, (data)=>{
            let result = []
            for( let key in data ){
              if(key==0){
                // 默认让当前页面显示列表第一个成员的信息
                this.sku_goods = data[key];
              }
              result[data[key].id] = data[key];
            }
            this.sku_list = result;
            this.get_attr_by_sku_id();
          });
        },
        get_attr_by_sku_id(){
          // 根据sku商品的id获取当前商品具体的商品属性
          rpc(settings.API, "Goods.sku_goods_attr",  {sku_id:this.sku_goods.id}, (data)=>{
            // 对数据进行重构
            this.sku_goods_attr = data;
          });
        }
      }
    });

  $(function(){
        // 商品图片
       var swiper = new Swiper('.swiper1', {
         pagination : '.pagination1',
         loop: true,
         paginationClickable: true,
         autoplay : 5000,
         grabCursor: true,
         autoHeight: true,
       });

       // 商品详情
       var swiper2 = new Swiper('.swiper2', {
         autoHeight: true,
         onSlideChangeStart: function(swiper){
           $('.page-btn span').eq(swiper.activeIndex).addClass('swiper-pagination-active').siblings().removeClass('swiper-pagination-active');
         }
       });

       // 按钮设置
       $('.page-btn span').click(function(){
         $(this).addClass('swiper-pagination-active').siblings().removeClass('swiper-pagination-active');
         swiper2.slideTo( $(this).index(), 500, false);
       });
  })
</script>
</body>
</html>

```

当用户选择不同的SKU商品时，发送ajax请求到后端查询数据

```vue
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-蘑菇网-你的专业导购</title>
  <meta name="Keywords" content="换季,新品" />
  <meta name="Description" content="换季,换季,换季,换季,换季,换季,换季,换季,换季" />
  <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
  <!-- Mobile Devices Support @begin -->
  <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
  <!-- Mobile Devices Support @end -->
  <link href="../css/index.css" rel="stylesheet" />
  <link href="../css/common.css" rel="stylesheet" />
  <link href="../css/swiper.min.css" rel="stylesheet" />
  <script src="../script/jquery-1.9.1.min.js"></script>
  <script src="../script/main.js"></script>
  <script src="../script/jquery.rotate.min.js"></script>
  <script src="../script/swiper.min.js"></script>
</head>
<body>
<div class="main" id="app">
  <!--头部-->
<div class="header" id="bktop">
  <div class="logo"><a href=""><img :src="'../'+siteconfig.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
          <ul class="xla">
              <li v-for="top in nav_list">
                  <a class="dianj dj1" :href="top.link"><font>{{top.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
                  <div class="zilan">
                      <a :href="son.link" v-for="son in top.children_list">{{son.name}}</a>
                  </div>
              </li>
          </ul>
      </div>
      <div class="clearBoth"></div>
  </div>
  <!--产品信息-->
  <div class="newsban"><a style="color:#ccc" href="">首页</a> > <a style="color:#ccc" href="">换季新品</a> > {{goods.title}} </div>
  <div id="main">
    <div class="home-device">
      <a class="arrow-left" href="#"></a>
      <a class="arrow-right" href="#"></a>
      <div class="swiper-main">
        <div class="swiper-container swiper1">
          <div class="swiper-wrapper">
            <div class="swiper-slide" v-for="item in goods_image"><img :src="item.image_url" width="100%"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="dian"><div class="pagination pagination1"></div></div>
  </div>
  <div class="newbt2" v-if="sku_goods.sale_price">{{sku_goods.name}} <span class="goods_price">￥{{sku_goods.sale_price.toFixed(2)}}</span></div>
  <ul class="sku_list">
      <li @click="change_sku_id(sku.id)" v-for="sku in sku_list" v-if="sku">{{sku.name}}</li>
  </ul>
  <div class="about">
    <div class="content2">
      <!-- start -->
      <div class="page-btn">
        <span class="swiper-pagination-active">商品详情</span>
        <span>商品参数</span>
        <span>同类热门</span>
      </div>
      <div class="swiper-container swiper2">
        <div class="swiper-wrapper" style="min-height: 500px;">
          <div class="swiper-slide product-content">
            <p class="image-list-title"><span>商品描述</span></p>
            <p class="product-desc">{{goods.descript}}</p>
            <p class="image-list-title"><span>穿着效果</span></p>
            <div class="product-desc" style="color: #fff;min-height: 100px;" v-html="goods.effect"></div>
          </div>
          <div class="swiper-slide product-param">
            <table class="parameter-table">
                <tr v-for="value,key in sku_goods_attr">
                    <td>{{key}}: {{value}}</td>
                </tr>
            </table>
          </div>
          <div class="swiper-slide">
            <div class="case_list">
              <div class="case_list_body case_list_body2 case_list_body3">
                <ul>
                  <li :class="key%2==0?'yyu':'casela'" v-for="item,key in hot_goods">
                      <a href="">
                        <div class="case_list_body_pic">
                          <img :src="'../'+item.image_url">
                        </div>
                      </a>
                      <div class="case_list_info">
                        <p class="cast_list_tit"><a href="">{{item.title}}</a></p>
                      </div>
                  </li>
                  <div class="clearBoth"></div>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!--底部-->
  <div class="bottom">
      <div class="bottom-top">
          <div class="linker">
              <div class="liuy">
                  <a href="">
                      <div class="tubiao"><img src="../image/liuy.gif" /></div>
                      <div class="wenzi">在线留言</div>
                      <div class="clearBoth"></div>
                  </a>
              </div>
              <div class="clearBoth"></div>
          </div>
      </div>
      <div class="bottom-bot">{{siteconfig.copyright}}</div>
  </div>
</div>
<script src="../script/vue.js"></script>
<script src="../script/axios.js"></script>
<script src="../script/tools.js"></script>
<script src="../script/settings.js"></script>
<script>
    var vm = new Vue({
      el:"#app",
      data:{
        siteconfig:{},
        nav_list:[
          {
            children_list:[],
          },{
            children_list:[],
          },{
            children_list:[],
          },
        ],
        goods:{},      // spu商品信息
        sku_goods:{},  // sku商品信息
        goods_image:[],
        hot_goods:[],
        sku_list:[],
        spu_id: 1,
        sku_id: 2,
        category: 0,
        sku_goods_attr:{}
      },
      watch:{
        sku_id(){
          // 监听sku_id的变化
          for(key in this.sku_list){
            if(this.sku_list[key].id == this.sku_id){
              this.sku_goods = this.sku_list[key];
            }
          }
          this.get_attr_by_sku_id();
        },
      },
      created(){
          this.get_site_config();
          this.get_nav_list();
          this.get_goods();
          this.get_goods_image();
          this.get_sku_by_spu_id();
      },
      methods:{
        change_sku_id(sku_id){
          // 切换不同的SKU商品ID
          this.sku_id = sku_id;
        },
        get_site_config(){
          // 獲取站點配置的api接口
          rpc(settings.API, "Common.siteconfig", {}, (data)=>{
            this.siteconfig = data;
          });
        },
        get_nav_list(){
          // 獲取導航菜單的api接口
          rpc(settings.API, "Common.nav", {}, (data)=>{
            this.nav_list = data;
          });
        },
        get_goods(){
          //. 获取商品详情的基本信息
          rpc(settings.API, "Goods.detail_goods", {id:this.spu_id}, (data)=>{
            this.goods = data;
            // 获取同类热门商品
            this.category = this.goods.category_id;
            this.get_hot_goods();
          });
        },
        get_goods_image(){
          // 获取当前商品相关的图片信息
          rpc(settings.API, "Goods.detail_goods_image", {id:this.spu_id}, (data)=>{
            this.goods_image = data;
          });
        },
        get_hot_goods(){
          // 获取当前商品的同类热门商品
          rpc(settings.API, "Goods.hot_goods", {goods_id:this.spu_id,category:this.category}, (data)=>{
            this.hot_goods = data;
          });
        },
        get_sku_by_spu_id(){
          // 通过SPU来获取所有的SKU库存商品
          rpc(settings.API, "Goods.detail_sku_goods", {spu_id:this.spu_id}, (data)=>{
            let result = []
            for( let key in data ){
              if(key==0){
                // 默认让当前页面显示列表第一个成员的信息
                this.sku_goods = data[key];
              }
              result[data[key].id] = data[key];
            }
            this.sku_list = result;
            this.get_attr_by_sku_id();
          });
        },
        get_attr_by_sku_id(){
          // 根据sku商品的id获取当前商品具体的商品属性
          rpc(settings.API, "Goods.sku_goods_attr",  {sku_id:this.sku_goods.id}, (data)=>{
            // 对数据进行重构
            this.sku_goods_attr = data;
          });
        }
      }
    });

  $(function(){
        // 商品图片
       var swiper = new Swiper('.swiper1', {
         pagination : '.pagination1',
         loop: true,
         paginationClickable: true,
         autoplay : 5000,
         grabCursor: true,
         autoHeight: true,
       });

       // 商品详情
       var swiper2 = new Swiper('.swiper2', {
         autoHeight: true,
         onSlideChangeStart: function(swiper){
           $('.page-btn span').eq(swiper.activeIndex).addClass('swiper-pagination-active').siblings().removeClass('swiper-pagination-active');
         }
       });

       // 按钮设置
       $('.page-btn span').click(function(){
         $(this).addClass('swiper-pagination-active').siblings().removeClass('swiper-pagination-active');
         swiper2.slideTo( $(this).index(), 500, false);
       });
  })
</script>
</body>
</html>

```













# 页面跳转

经过前面的开发，我们整个APP项目大部分数据都已经输出到页面中，接下来我们需要让这些页面之间能够进行跳转，在用户点击按钮的时候打开新的页面窗口。

```html
# 打开一个新的窗口
api.openWin({
	name:"窗口名称",  // 必须定义一个窗口名称，方便后面操作这个窗口
	url: "",
	pageParam:{     // 发送给新窗口的参数
		 参数名:参数值,
		 参数名:参数值,
	}
})

# 关闭当前窗口
api.closeWin();
# 关闭指定名称的窗口
api.closeWin({
	name:"窗口名称",
});

# 新窗口接受上一个窗口api.openWin()的参数
api.pageParam       # 获取所有参数
api.pageParam.参数名 # 获取指定参数


    // 在当前窗口中打开一个框架
    api.openFrame({
      name: 'page2',  // 自定义框架名称
      url: './products.html',
      rect: {
          x: 50, // 当前框架距离左上角的x轴
          y: 50, // 当前框架距离左上角的y轴
          w: 200,  // 当前框架的宽度,'auto'占满
          h: 250   // 当前框架的高度,'auto'占满
      },
      pageParam: {   // 参数
          name: 'test'
      }
    });
```

### 添加导航测试

```sql
UPDATE `mogu_nav` SET link='./html/products.html' where id = 6;
UPDATE `mogu_nav` SET link='./html/products.html' where id = 4;
UPDATE `mogu_nav` SET link='./html/products.html' where id = 5;

UPDATE `mogu_nav` SET link='./html/news.html' where parent_id=2;
UPDATE `mogu_nav` SET link='./html/news_detail.html' where parent_id=3;

```



## 购物车

```python
1. 购物车通过axios发送请求到后端保存数据，数据存储在redis中。

2. redis数据库保存购物车胡数据结构：
	cart_<user_id>: {
  	<goods_id>: <goods_num>,
	}
  select_<user_id>:{
  	goods_id,
    goods_id,
  }

3. 完成添加商品到购物车页面的功能以后，我们可以通过APICloud提供的AUI来实现购物车的基本界面效果。 

4. 新建一个页面作为购物车商品列表，参考路飞的购物车商品列表页面，实现勾选的功能。

5. 当在购物车商品列表页中，继续点击"立即付款"，这种类似的按钮时，通过js来获取勾选的商品信息，来商城订单。

6. 对于在蘑菇街中的订单，也是分成2个表，一个事订单信息表，和路飞学城的一模一样，另外有一张订单详情表，这张中把购物车商品的有效期选项去掉，新增一个商品数量。

7. 在生辰订单以后，在服务端返回结果以后，调用 APIColud提供的模块微信支付模块完成从蘑菇街跳转到
微信的功能，当然，我们要有对应的微信支付接口才可以完成这个留个，不过，这个流程和支付宝很类似。

```

## flask的第三方模块

#### flask-admin模块

flask-admin ，类似django-admin的后台管理工具

http://flask123.sinaapp.com/article/57/

安装flask-admin

```python
pip install flask-admin
```

在`apps/__init__.py`进行初始化

```python
from flask import Flask
from redis import StrictRedis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from apps.settings.dev import DevelopementConfig
from apps.settings.prod import ProductionConfig
from apps.utils.log import init_log

from flask_jsonrpc import JSONRPC
from flask_jsonrpc.site import JSONRPCSite

# 创建jsonrpc实例对象
jsonrpc_v1 = JSONRPC(service_url="/api/v1", site=JSONRPCSite(), enable_web_browsable_api=True)
jsonrpc_v2 = JSONRPC(service_url="/api/v2", site=JSONRPCSite(), enable_web_browsable_api=True)
config = {
	"dev": DevelopementConfig,
	"prop": ProductionConfig,
}

# 预设全局变量
redis_store = None
db = SQLAlchemy()

def init_app(config_name):
	"""项目的初始化功能"""
	app = Flask(__name__)
  
  # 。。。。

	# flask-admin进行app初始化
	# flask-admin的初始化
	app.admin = Admin(app=None, name='蘑菇街', template_mode='bootstrap3')
	app.admin.init_app(app)

	return app
```

在manage.py中进行注册

```python
# 把模型注册到flask-admin后台运营站点
from flask_admin.contrib.sqla import ModelView
class MyModelView(ModelView):
    pass
app.admin.add_view( MyModelView(SiteConfig,db.session,name="站点配置") )
app.admin.add_view( MyModelView(Nav,db.session,name="导航菜单") )
app.admin.add_view( MyModelView(Banner,db.session,name="轮播广告") )
app.admin.add_view( MyModelView(GoodsCategory,db.session,name="商品分类") )
app.admin.add_view( MyModelView(SPU,db.session,name="商品SPU") )
```

效果：

![1567764568747](../../../%E6%B7%B1%E5%9C%B35%E6%9C%9F/5-%E8%98%91%E8%8F%87%E8%A1%97APP%E9%A1%B9%E7%9B%AE/day04/assets/1567764568747.png)



## flask-login

flask-login，类似django-auth提供的登录功能

<https://www.jianshu.com/p/01384ee741b6>





## Gunicorn

高性能的web服务器软件，经常用于配合flask框架搭建web网站服务。

官网地址：https://gunicorn.org/

安装命令：

```python
pip install gunicorn
```

在项目的根目录下面终端，可以使用以下命令来启动项目：

```python
gunicorn -w 4 -b 0.0.0.0:5000 manage:app
# gunicorn -w 工作进程 -b 绑定IP:绑定端口 终端脚本文件名:flask实例对象
```

当然我们，一般运行Gunicorn不会一直卡在终端下面运营，肯定以守护进行的方式来运行。

```python
gunicorn -w 4 -b 0.0.0.0:5000 -c 配置文件.py manage:app
```

配置文件，配置项如下：

```python
import multiprocessing

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1

backlog = 2048
worker_class = "gevent"
worker_connections = 1000
daemon = True
debug = False
proc_name = 'gunicorn_demo'
pidfile = './logs/gunicorn.pid'
errorlog = './logs/gunicorn.log'
```

再次启动就可以了。

```python
gunicorn -c gunicorn.py manage:app
```


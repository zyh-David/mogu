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
    type_id= db.Column(db.Integer, db.ForeignKey("mogu_goods_type.id"),comment="类型ID")
    total_sale = db.Column(db.Integer, comment="总销量")
    total_number = db.Column(db.Integer, comment="总库存量")
    def __repr__(self):
        return "%s" % (self.title)

# 商品库存[sku]   mogu_goods_sku
class GoodsSKU(BaseModel, db.Model):
    """商品库存信息"""
    __tablename__ = "mogu_goods_sku"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    title = db.Column(db.String(500), nullable=True, comment="商品库存名称")
    spu_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_spu.id"), comment="商品系列ID")
    sale = db.Column(db.Integer, comment="单品销量")
    number = db.Column(db.Integer, comment="库存量")
    price = db.Column(db.Numeric(8, 2), comment="商品进货价")
    sale_price = db.Column(db.Numeric(8, 2), comment="商品销售价")
    attr_list = db.relationship('GoodsSKUAttribute', backref='sku_attr', lazy='dynamic')
    img_list = db.relationship('GoodsImage', backref='sku_image', lazy='dynamic')

    def __repr__(self):
        return "%s" % (self.title)

# 商品图片        mogu_goods_image
class GoodsImage(BaseModel, db.Model):
    """商品图片"""
    __tablename__ = "mogu_goods_image"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    image_url = db.Column(db.String(256), default='', comment="封面图片")
    sku_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_sku.id"), default=0, nullable=True, comment="SKU_ID")

    def __repr__(self):
        return "%s" % (self.image_url)

# 商品类型        mogu_goods_type
class GoodsType(BaseModel, db.Model):
    """商品类型"""
    __tablename__ = "mogu_goods_type"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    name = db.Column(db.String(64), nullable=True, comment="类型名称")
    goods_spu_list = db.relationship('GoodsSPU', backref='spu_type', lazy='dynamic')
    attr_list = db.relationship('GoodsAttribute', backref='attr_type', lazy='dynamic')

# 商品属性        mogu_goods_attr
class GoodsAttribute(BaseModel, db.Model):
    """商品属性"""
    __tablename__ = "mogu_goods_attribute"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    name = db.Column(db.String(64), nullable=True, comment="属性名称")
    type_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_type.id"), comment="类型ID")
    value_type = db.Column(db.Enum("唯一值", "单选值"), default="唯一值")
    input_type = db.Column(db.Enum("手动录入", "下拉列表"), default="手动录入")
    option_list = db.relationship('GoodsAttributeOption', backref='option_arrtibute', lazy='dynamic')
    goods_list = db.relationship("GoodsSKUAttribute",backref="goods_attribute",lazy="dynamic")

# 商品属性选项     mogu_goods_attr_option
class GoodsAttributeOption(BaseModel, db.Model):
    """商品属性值选项"""
    __tablename__ = "mogu_goods_attribute_option"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    attr_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_attribute.id"), comment="属性ID")
    option = db.Column(db.String(64), nullable=True, comment="选项值")


# 商品具体属性值   mogu_goods_attr_option
class GoodsSKUAttribute(BaseModel, db.Model):
    """SKU商品属性值"""
    __tablename__ = "mogu_goods_sku_attribute"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    sku_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_sku.id"), comment="SKU_ID")
    attr_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_attribute.id"), comment="属性ID")
    option_id = db.Column(db.Integer, db.ForeignKey("mogu_goods_attribute_option.id"), default=0, nullable=True,
                          comment="属性ID")
    value = db.Column(db.String(640), nullable=True, comment="属性值")
from apps import jsonrpc_v1
from .models import db, GoodsSPU, GoodsCategory,GoodsSKU,GoodsImage,GoodsSKUAttribute,GoodsAttributeOption

@jsonrpc_v1.method("Goods.home_goods")
def home_goods():
	"""首页今日"心"品"""
	goods_list = GoodsSPU.query.filter(
		GoodsSPU.is_show==True,
		GoodsSPU.is_deleted==False,
		GoodsSPU.is_recommend==True
	).order_by(
		GoodsSPU.sort.asc(),
		GoodsSPU.id.desc()
	).limit(5).all()

	data = []
	for goods in goods_list:
		"""把列表中每个对象转换成字典"""
		data.append( goods.__to_dict__(["id","title","image_url"]) )
	return data

@jsonrpc_v1.method("Goods.goods_category")
def goods_categoty():
	"""商品分类"""
	cat_list = GoodsCategory.query.filter(
		GoodsCategory.is_show==True,
		GoodsCategory.is_deleted==False
	).order_by(
		GoodsCategory.sort.asc(),
		GoodsCategory.id.desc()
	).limit(6).all()

	data = []
	for category in cat_list:
		"""把列表中每个对象转换成字典"""
		data.append( category.__to_dict__(["id", "name"]) )

	return data

@jsonrpc_v1.method("Goods.list_goods(category=int,page=int,size=int)")
def list_goods(category=None, page=1, size=10):
	"""商品列表"""
	query = GoodsSPU.query.filter(
		GoodsSPU.is_show==True,
		GoodsSPU.is_deleted==False
	)

	if category is not None:
		query = query.filter(GoodsSPU.category_id==category)

	paginate = query.order_by(
		GoodsSPU.sort.asc(),
		GoodsSPU.id.desc()
	).paginate(page,size)

	# 分页器也要转换成字典
	data = {}
	data["page"] = paginate.page
	data["pages"] = paginate.pages
	data["has_prev"] = paginate.has_prev
	data["has_next"] = paginate.has_next
	data["next_num"] = paginate.next_num
	data["prev_num"] = paginate.prev_num
	# 设置分页器里面的每一页数据项
	data["items"] = []
	for goods in paginate.items:
		"""把列表中每个对象转换成字典"""
		data["items"].append( goods.__to_dict__(["id","title","image_url"]) )

	return data

@jsonrpc_v1.method("Goods.detail_spu_goods(spu_id=Number)")
def detail_spu_goods(spu_id):
	"""详情页spu商品信息"""
	data = {}
	try:
		goods = GoodsSPU.query.filter(
					GoodsSPU.id==spu_id
				).first()
		goods.category_name = goods.category.name
		data = goods.__to_dict__(["id", "title", "descript","effect","category_id","category_name"])
	except:
		pass

	return data


@jsonrpc_v1.method("Goods.detail_hot_goods(category=Number,limit=Number)")
def detail_hot_goods(category,limit=6):
	"""商品详情的同类热门"""
	query = GoodsSPU.query.filter(
		GoodsSPU.is_show == True,
		GoodsSPU.is_deleted == False,
		GoodsSPU.category_id == category,
	).order_by(
		GoodsSPU.sort.asc(),
		GoodsSPU.total_sale.desc(),  # 根据销量来判断是否热门
		GoodsSPU.id.desc()
	)
	goods_list = query.limit(limit).all()
	data = []
	for goods in goods_list:
		item = goods.__to_dict__(["id", "title", "image_url"])
		data.append(item)
	return data


@jsonrpc_v1.method("Goods.detail_sku_goods(spu_id=Number)")
def detail_sku_goods(spu_id):
	"""当前系列下的所有的sku库存"""
	goods_list = GoodsSKU.query.filter(
		GoodsSKU.is_show == True,
		GoodsSKU.is_deleted == False,
		GoodsSKU.spu_id == spu_id,
	).order_by(
		GoodsSKU.sort.asc(),
		GoodsSKU.id.desc()
	).all()

	data = []
	for sku in goods_list:
		sku.sale_price = float(sku.sale_price)
		item = sku.__to_dict__(["id", "title","sale","sale_price"])
		data.append(item)
	return data

@jsonrpc_v1.method("Goods.detail_sku_goods_image(sku_id=Number)")
def detail_sku_goods_image(sku_id):
	"""获取sku对应的所有商品图片"""
	img_list = GoodsImage.query.filter(
		GoodsImage.is_show == True,
		GoodsImage.is_deleted == False,
		GoodsImage.sku_id == sku_id,
	).order_by(
		GoodsImage.sort.asc(),
		GoodsImage.id.desc()
	).all()

	data = []
	for img in img_list:
		item = img.__to_dict__(["image_url"])
		data.append(item)
	return data

@jsonrpc_v1.method("Goods.detail_sku_goods_attr(sku_id=Number)")
def detail_sku_goods_attr(sku_id):
	"""根据sku_id获取商品属性"""
	attr_list = GoodsSKUAttribute.query.filter(
		GoodsSKUAttribute.is_show == True,
		GoodsSKUAttribute.is_deleted == False,
		GoodsSKUAttribute.sku_id==sku_id
	).order_by(
		GoodsSKUAttribute.sort.asc(),
		GoodsSKUAttribute.id.desc()
	).all()

	attr_dict = {}
	for attr in attr_list:
		arrt_name = attr.goods_attribute.name
		value     = GoodsAttributeOption.query.get(attr.value).option
		attr_dict[arrt_name] = value

	return attr_dict
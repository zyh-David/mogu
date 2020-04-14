from apps import jsonrpc_v1
from .models import db, Nav, Banner, SiteConfig

@jsonrpc_v1.method("Home.banner")
def banner():
	"""轮播广告"""
	banner_list = Banner.query.filter(
		Banner.is_show==True,
		Banner.is_deleted==False
	).order_by(
		Banner.sort.asc(),
		Banner.id.desc()
	).limit(8).all()

	data = []
	for banner in banner_list:
		"""把列表中每个对象转换成字典"""
		data.append( banner.__to_dict__(["id","image_url","link"]) )
	return data


@jsonrpc_v1.method("Home.site_config")
def site_config():
	"""站点配置"""
	site_config_list = SiteConfig.query.filter(
		SiteConfig.is_show==True,
		SiteConfig.is_deleted==False
	).order_by(
		SiteConfig.sort.asc(),
		SiteConfig.id.desc()
	).limit(8).all()

	data = {}
	for item in site_config_list:
		result = item.__to_dict__(["name","value"])
		data[result["name"]] = result["value"]
	return data

@jsonrpc_v1.method("Home.nav")
def nav():
	"""导航信息"""
	# 先获取顶级菜单
	top_list = Nav.query.filter(
		Nav.is_show == True,
		Nav.is_deleted == False,
		Nav.parent_id == None,
	).order_by(
		Nav.sort.asc(),
		Nav.id.asc()
	)

	data = []
	for top in top_list:
		# 获取当前导航的所有子导航
		top.children_list = []
		for son in top.children:
			top.children_list.append(son.__to_dict__(["name","link"]))
		data.append(top.__to_dict__(["name","link","children_list"]))
	return data
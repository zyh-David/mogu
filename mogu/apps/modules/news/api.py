from apps import jsonrpc_v1
from .models import db, News, NewsCategory

@jsonrpc_v1.method("News.home_news")
def home_news():
	"""首页潮流资讯"""
	news_list = News.query.filter(
		News.is_show==True,
		News.is_deleted==False,
		News.is_recommend==True
	).order_by(
		News.sort.asc(),
		News.id.desc()
	).limit(5).all()

	data = []
	for news in news_list:
		"""把列表中每个对象转换成字典"""
		data.append( news.__to_dict__(["id","title","image_url","descript","read_count","created_time"]) )
	return data

@jsonrpc_v1.method("News.news_category")
def news_category():
	"""文章分类"""
	category_list = NewsCategory.query.filter(
		NewsCategory.is_show==True,
		NewsCategory.is_deleted==False
	).order_by(
		NewsCategory.sort.asc(),
		NewsCategory.id.desc()
	).limit(6).all()

	data = []
	for category in category_list:
		"""把列表中每个对象转换成字典"""
		data.append( category.__to_dict__(["id","name"]) )
	return data

@jsonrpc_v1.method("News.list_news(category=int,page=int,size=int)")
def list_news(category=None, page=1, size=10):
	"""文章列表"""
	query = News.query.filter(
		News.is_show==True,
		News.is_deleted==False
	)

	if category is not None:
		query = query.filter(News.category_id==category)

	paginate = query.order_by(
		News.sort.asc(),
		News.id.desc()
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
	for news in paginate.items:
		"""把列表中每个对象转换成字典"""
		data["items"].append( news.__to_dict__(["id","title","image_url","descript","read_count","created_time"]) )

	return data

@jsonrpc_v1.method("News.news(id=int)")
def list_news(id):
	"""文章详情"""
	news = News.query.filter(
		News.is_show==True,
		News.is_deleted==False,
		News.id==id
	).first()

	# 每一次有人访问了当前文章,则表示当前文章的阅读量+1
	news.read_count+=1
	db.session.commit()
	news.category_name = news.category.name
	data = news.__to_dict__(["title","category_name","read_count","created_time","content","author"])

	return data
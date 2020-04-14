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
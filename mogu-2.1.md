# 基于Flask-JSONRPC提供RPC接⼝

JSON-RPC是一个无状态的、轻量级的远程过程调用（RPC）协议。

所谓的RPC，`Remote Procedure Call`的简写，中文译作**远程过程调用**或者**远程服务调用**。

直观的理解就是，通过网络来请求服务，获取接口数据，而不用知晓底层网络协议的细节。

`RPC`支持的格式很多，比如`XML`格式，`JSON`格式等等。最常用的肯定是json-rpc。



JSON-RPC协议中的客户端一般是为了向远程服务器请求执行某个方法/函数。客户端向实现了JSON-RPC协议的服务端发送请求，多个输入参数能够通过数组或者对象传递到远程方法，这个远程方法也能返回多个输出数据，具体是什么，当然要看具体的方法实现。

所有的传输都是单个对象，用JSON格式进行序列化。

请求要求包含三个特定属性：

```
jsonrpc: 用来声明JSON-RPC协议的版本，现在基本固定为“2.0”

method，方法，是等待调用的远程方法名，字符串类型

params，参数，对象类型或者是数组，向远程方法传递的多个参数值

id，任意类型值，用于和最后的响应进行匹配，也就是这里设定多少，后面响应里这个值也设定为相同的
响应的接收者必须能够给出所有请求以正确的响应。这个值一般不能为Null，且为数字时不能有小数。
```

响应也有三个属性：

```
jsonrpc: 用来声明JSON-RPC协议的版本，现在基本固定为“2.0”

result，结果，是方法的返回值，调用方法出现错误时，必须不包含该成员。

error，错误，当出现错误时，返回一个特定的错误编码，如果没有错误产生，必须不包含该成员。

id，就是请求带的那个id值，必须与请求对象中的id成员的值相同。请求对象中的id时发生错误（如：转换错误或无效的请求），它必须为Null
```

当然，有一些场景下，是不用返回值的，比如只对客户端进行通知，由于不用对请求的id进行匹配，所以这个id就是不必要的，置空或者直接不要了。



在flask中要实现提供json-rpc接口，开发中一般使用**Flask JSON-RPC**模块来实现。

git地址：https://github.com/cenobites/flask-jsonrpc

文档：http://wiki.geekdream.com/Specification/json-rpc_2.0.html



### 安装Flask-JSONRPC模块

```shell
pip install Flask-JSONRPC==0.3.1
```

快速实现一个测试的RPC接口。

例如，我们直接在manage.py启动文件中直接实现。

```python
from apps import init_app,db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_jsonrpc import JSONRPC

app = init_app("dev")

# 使用终端脚本工具启动和管理flask
manager = Manager(app)

# 启用数据迁移工具
Migrate(app, db)
# 添加数据迁移的命令到终端脚本工具中
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
  return 'hello,moluo~'

# 初始化jsonrpc模块
jsonrpc = JSONRPC(app, '/api')

# 实现rpc接口
@jsonrpc.method('Common.index')
def index():
    return u'Welcome to Flask JSON-RPC'


if __name__ == '__main__':
    manager.run()
```



客户端需要发起post请求，访问地址为：`http://服务器地址:端口/api`

#### 注意

默认情况下，`/api`接口只能通过post请求访问。如果要使用jsonrpc提供的界面调试工具，则访问地址为：

```python
http://服务器地址端口/api/browse/
```



访问数据格式应是：

```json
{
    "jsonrpc": "2.0",
    "method": "Common.index",
    "params": {},
    "id": "1"
}
```



通过postman访问效果：

![1559505655439](assets/1559505655439.png)





### 对RPC接口代码进行模块化分离

把jsonrpc模块的初始化代码抽离到app对象初始化函数init__app函数中。

`apps/__init__py`，代码：

```python
from flask import Flask
from redis import StrictRedis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_jsonrpc import JSONRPC

from apps.utils.log import init_log
from apps.settings.dev import DevelopementConfig
from apps.settings.prop import ProductionConfig

config = {
    "dev": DevelopementConfig,
    "prop": ProductionConfig,
}

# 预设全局变量
redis_store = None
db = SQLAlchemy()
# 创建jsonrpc实例对象
jsonrpc = JSONRPC(app=None, service_url='/api', enable_web_browsable_api=True)

def init_app(config_name):
    """项目的初始化功能"""
    app = Flask(__name__)

    # 设置配置类
    Config = config[config_name]

    # 加载配置
    app.config.from_object(Config)

    # redis的链接初始化
    global redis_store
    redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,db=0)

    # 开启session功能
    Session(app)
    
    # 配置数据库链接
    db.init_app(app)

    # 启动日志
    init_log(Config)

    # jsonrpc注册到app应用对象中
    jsonrpc.init_app(app)

    return app
```



modules/home/api.py，代码：

```python
from apps import jsonrpc
# 实现rpc接口
@jsonrpc.method('Common.index')
def index():
    return u'Welcome to Flask JSON-RPC'
```

manage.py启动文件中加载api接口

```python
from apps import init_app,db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = init_app("dev")

# 使用终端脚本工具启动和管理flask
manager = Manager(app)

# 启用数据迁移工具
Migrate(app, db)
# 添加数据迁移的命令到终端脚本工具中
manager.add_command('db', MigrateCommand)

# api接口列表
from home import api

@app.route('/')
def index():
  return 'hello,moluo~'

if __name__ == '__main__':
    manager.run()
```

重新启动项目，使用postman进行还是原来的结果，则表示调整成功，后面的开发中，我们只需要不断增加对应的接口即可。

在postman下面发送请求,请求地址:	POST   http://39.108.194.129:5000/api

```python
# 请求体格式: json

# 请求体数据

{
	"jsonrpc": "2.0",
	"method": "Common.index",
	"params": [],
	"id": "1"
}
```





### 使用jsonrpc接受客户端请求的参数

服务器提供rpc接口方法：

```python
from apps import jsonrpc

@jsonrpc.method("模块名.方法名(参数变量名=数据类型, password=String)")
def 方法名(参数变量名,password):
    return u"参数变量名：%s，密码：%s" % (参数变量名,password)
```

服务端api接口提供了rpc接受5种不同的数据类型:

```python
Number 数值类型
String 字符串类型
Object 对象类型
Array  数组列表类型
Boolean 布尔值类型
```



客户端发送请求：

```python
{
	"jsonrpc": "2.0",
	"id": 188,
	"method": "Common.add",
	"params": {
		"username":"xiaohui",
		"age":33,
		"sex":false,
		"lve":["吃饭","睡觉",3,4,{"title":"aaaa"}],
		"son":{
			"username":"xiaohuihui",
			"age":12
		}
	}
}
```



#### 实现jsonrpc接口的版本迭代

基于flask_jsonrpc.site.JSONRPCSite 来实现

`apps/__init__`代码：

```python
from flask import Flask
from redis import StrictRedis
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_jsonrpc import JSONRPC
from flask_jsonrpc.site import JSONRPCSite
from apps.settings.dev import DevelopementConfig
from apps.settings.prop import ProductionConfig
from apps.utils.log import init_log

config = {
  "dev": DevelopementConfig,
  "prop": ProductionConfig,
}

# 预设全局变量
redis_store = None
db = SQLAlchemy()
# jsonrpc实例化
jsonrpc_v1 = JSONRPC(service_url="/api/v1", site=JSONRPCSite(), enable_web_browsable_api=True)
jsonrpc_v2 = JSONRPC(service_url="/api/v2", site=JSONRPCSite(), enable_web_browsable_api=True)


def init_app(config_name):
  
  。。。。

  # 启动日志
  init_log(Config)

  # 把jsonrpc注入到app实例对象中
  jsonrpc_v1.init_app(app)
  jsonrpc_v2.init_app(app)

  return app

```

模块目录modules/common/api.py，代码：

```python
from apps import jsonrpc_v1, jsonrpc_v2

@jsonrpc_v1.method('Common.index(id=int, sex=bool, name=str,lve=Array, son=Object)')
def index(id,sex,name,lve,son):
    print("id=%s,sex=%s,name=%s,lve=%s,son=%s" % (id,sex,name,lve,son) )
    return u'Welcome to mogujie,id=%s' % id

@jsonrpc_v2.method('Common.index(id=int, sex=bool, name=str,lve=Array, son=Object)')
def index2(id,sex,name,lve,son):
    return u"id=%s,sex=%s,name=%s,lve=%s,son=%s" % (id,sex,name,lve,son)
```

最终效果：

![1567736773039](assets/1567736773039.png)

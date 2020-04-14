# 移动端开发相关概念

![20170511142800107.png](assets\20170511142800107.png)

## APP类型

![img](assets\13133049-92942339334ee062.webp)

### Native APP

Native APP又称原生APP，就是我们平时说的手机应用软件。

原生APP 是针对IOS、Android、Windows等不同的手机操作系统要采用不同的语言和框架进行开发出来的，通常是由“云服务器数据+APP应用客户端”两部份构成。

实现技术：

```
iOS: Object-C 或者 swift
Android: java
```



#### 优缺点

```txt
优点：
		体验好，用户无法上网也可访问APP应用中以前下载的数据
		性能稳定，可调用手机的硬件设备（语音、摄像头、短信、GPS、重力感应等）和本地资源（通讯录，相册等）
		操作速度快，能够实现出色的动效，转场动画
		
缺点：
		开发周期长，开发人员工资起点高。
		用户要使用原生APP，必须通过安装到手机里面才行，而且APP软件体积大，占用较多手机内存容量
		更新缓慢，根据不同平台，提交–审核–上线流程较复杂。
		要获取最新功能，需要升级应用，所以会容易出现有些用户不升级，导致多个不同功能版本出现，维护成本大
		跨平台差，每种平台都需要独立的开发语言。Java(安卓),Objective-C(iOS)等等
```



### Web APP

Web APP本质上是为移动浏览器设计的网站，可以在各种智能手机浏览器上运行。

实现技术：

```
HTML5+Javascript+CSS3
vue组件化+项目打包
....
```



#### 优缺点

```txt
优点：
		一套代码到处运行，可以同时在 PC、Android、iPhone 浏览器上访问
		开发者不需要发布到应用市场审核，用户不需要下载、安装和更新
		开发周期短，维护成本低
		用户不需用户手动更新，可以自动更新，直接使用最新版本

缺点：
		转场表现略差，要求联网
		用户体验没那么炫。图片和动画支持性不高
		没法在App Store中下载、无法通过应用下载获得盈利机会
		对手机功能应用缺乏，有限制（摄像头、GPS、蓝牙等）
```



### Hybrid APP

Hybrid App就是混合APP，就是Native结合Web的混合开发，就是内部本质是Web网页，使用打包软件给它套一层原生APP的外壳。

实现技术：

```
React Native
phoneGap(cordova+android)
APICloud
WeX5
appMobi
appcan
....
```



#### 优缺点

```txt
优点：
		集众家之长，既可以调用丰富的手机设备API，也能拥有Web APP的跨平台能力
		可以在应用商店发布，实现收费下载
		内部是网页结构，可以自主更新，做到开发一次，所有平台生效
		降低开发成本和技术成本，降低维护和开发周期
缺点：
		本质上就是一个Web APP使用了原生APP的壳，所以体验比不上原生APP
		开发难度比Web APP高，有一定的学习成本，开发周期比Web APP长
		APP发布有可能无法通过审核，需要多次调整，才能发布
		依赖开发框架本身提供的手机设备API，少部分设备功能还是只能借住原生语言进行调用才可以
		对团队技术栈要求相对高，既要懂web开发的，也要懂原生APP开发的
```



## 移动端屏幕介绍

![移动端屏幕](.\assets\rem-11.png)



## 移动端自适配方案

目前常用的布局适配方案就3种，分别是`vw`、`像素百分比+flex布局`和`rem+viewport`，后者最流行最容易。

当然，`rem+viewport`这种方案的实现方式也有很多，其中最著名的就是淘宝的**[flexible方案](https://github.com/amfe/article/issues/17)**。



## 元信息（meta）

meta标签，也叫元信息标签。作用就是用来告诉浏览器，当前网页的附加信息。

meta标签主要有2个属性比较重要。

| 属性名     | 属性值                                        | 作用描述           |
| :--------- | :-------------------------------------------- | :----------------- |
| http-equiv | content-type , expires , refresh , set-cookie | 设置 **HTTP 头部** |
| name       | viewport，author , description , keywords     | 设置网页附加信息   |

例子：

```python
<head>
	<meta name="description" content="移动端开发" />
  <meta name="keywords" content="移动端,APP,flask" />
  
	<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
	<meta http-equiv="Refresh" content="5;url=http://www.w3school.com.cn" />
</head>
```



### 视口（Viewport）

视口是一个相对比较复杂的概念，所以我们可以简单的理解为，viewport就是用户看手机页面时的可视区域，相当于桌面浏览器的窗口。在桌面浏览器中，viewport 就是浏览器窗口的宽度高度。但在移动端设备上就有点太窄了。

关于视口的详细扩展知识可以参看：https://www.w3cplus.com/css/viewports.html



视口通过meta标签进行设置

```html
<meta name="viewport" content="width=device-width, initial-scala=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
```



视口参数说明

| 属性名        | 属性值                   |
| ------------- | ------------------------ |
| device-width  | 设备的宽度               |
| initial-scale | 初始的缩放比例           |
| minimum-scale | 允许用户缩放到的最小比例 |
| maximum-scale | 允许用户缩放到的最大比例 |
| user-scalable | 用户是否可以手动缩放     |



### 像素（pixel）

在移动端上，所谓的像素分为两种。

CSS像素：CSS像素就是我们在编写CSS代码时的像素。

设备像素：设备屏幕的物理像素，任何设备的物理像素的数量都是固定的。



### 媒体查询（media query）

媒体查询是css3的一个新增语法属性，它根据页面的视口宽度来定义特殊的 CSS 规则，一般用于进行移动端适配。

```css
@media screen and (min-width:600px) and (max-width:900px){
  body {background-color:#f5f5f5;}
}
```



# 开发准备

我们接下来开发的项目是蘑菇街APP，主要通过APICloud+Flask完成。



## 注册APICloud帐号

APICloud官网：https://www.apicloud.com

开发文档：https://docs.apicloud.com

![1559241638547](assets\1559241638547.png)



## 下载APP开发编辑器

注册成功，登录进入开发控制台，找到页面右下角点击<mark>开发工具</mark>跳转到工具下载页面。

![1559241831748](assets/1559241831748.png)



网站地址：https://www.apicloud.com/devtools

![1559241890823](assets/1559241890823.png)





下载完成以后，无需安装，直接解压，打开编辑器并登录APICloud。

![1559242029172](assets/1559242029172.png)



![1559242103189](assets/1559242103189.png)



## 下载APP开发调试工具

在前面登录的APICloud开发控制台中，找到页面右下角点击<mark>SDK下载</mark>跳转到工具下载页面。

![1559242387164](assets/1559242387164.png)



网址：https://docs.apicloud.com/Download/download

点击<mark>AppLoader</mark>下载APP加载器工具，如扫码无法下载，则手动下载压缩包，通过USB连接电脑拖动到手机中进行安装。

![1559242428112](assets/1559242428112.png)



安装完成效果：

![1559242858133](assets/1559242858133.png)



## 下载手机共屏工具 Total Control

网址：http://tc.sigma-rt.com.cn/

注意

```
1. 当前工具目前仅支持安卓手机，如果是IOS，可以选择使用iTools进行共屏
2. 原则上来说，这个工具其实不用也可以，如果觉得一边开发一边操作手机麻烦的话，可以安装一下。
```



![1559242928800](assets/1559242928800.png)



下载<mark>稳定版</mark>即可，安装步骤省略。安装完成以后，使用USB连接线，连接电脑和手机。

注意：

```
1. USB线如果损坏或者年代久远只能充电，自己去买一根回来。
2. 如果电脑使用WiFi连接，也可以通过把手机和电脑连载一个wifi下进行开发共屏。
3. 共屏，需要手机设置开发者模式，每一台手机都会提供开发者模式的，不同型号手机，可以查看软件介绍，也可以自行百度。
4. 共屏使用USB连接线的话，需要手机开启USB调试功能。一般是打开设置->关于手机->手机版本号
   拼命戳版本号几次，就可以开启了。如果不能，可以自行百度。
```



点击启动Total Control，效果如下：

![1559242608343](assets/1559242608343.png)



等待检测设备，如果识别不了，很有可能就是你的手机USB连接线出问题了，换掉吧。

![1559242636330](assets/1559242636330.png)



手机连接成功效果： 

![1559242791247](assets/1559242791247.png)



点击<mark>连接</mark>，进行手机投屏到电脑上。

![1559242804678](assets/1559242804678.png)



如果出现以下窗口，一般以下三个原因：

```
1. USB线损坏或不支持调试，换一根把。
2. 插口松了
3. 手机开发者模式没开启或者USB调试功能没开启
4. 有多余的软件阻止了共屏，360安全位置呀，防火墙呀，电脑管家呀，杀毒软件呀，谷歌浏览器的都关了吧。
```

![1559242732629](assets/1559242732629.png)



最终共屏效果：

![1559243711305](assets/1559243711305.png)





# 项目搭建

## 移动端项目搭建

在打开的APICloud编辑器中点选<mark>新建项目</mark>即可。

![1559242164747](assets/1559242164747.png)



填写项目相关选项。

![1559243937939](assets/1559243937939.png)



创建项目成功。

![1559243998792](assets/1559243998792.png)

接下来，可以打开index.html页面，这是APP的欢迎页面。

![1559244068376](assets/1559244068376.png)



### 真机调试

好了，接下来我们可以通过APICloud开发工具，生成一个临时的APP，查看效果。

这个步骤，我们叫<mark>真机调试</mark>。

鼠标右键点击左上角的项目目录，点选菜单中的<mark>USB同步(xxx)</mark>选项。

![1559244166348](assets/1559244166348.png)

测试效果：

![1559244234084](assets/1559244234084.png)

![1559244277316](assets/1559244277316.png)



如果编辑器右上角出现的不是绿色弹窗，则证明调试失败！

此时检测是否是USB连接线出问题了！换一条吧，不贵的。





## 服务端项目搭建

### 云服务器购买

![1559483870448](assets/1559483870448.png)



### 安装基本软件

#### 1. 远程链接服务器

```shell
ssh 用户名@ip地址
# 也可以使用xshell或者其他软件在window下链接服务器。
```



#### 2. 服务器准备工作

##### 2.0 先更新 apt 相关源

```
sudo apt-get update
```



##### 2.1 安装git

```shell
sudo apt-get install git
```



##### 2.2 mysql安装

```
apt-get install mysql-server
apt-get install libmysqlclient-dev
```

进入数据库, 刚安装完成的数据库，root是空密码，所以要修改root的密码

```sql
mysql -uroot -p

# 修改密码
use mysql;
update user set authentication_string=password('新密码') where user='root' and Host ='localhost';
update user set plugin="mysql_native_password"; 

# 刷新权限
flush privileges;
```

创建数据库命令如下：

```sql
create database moguapp charset=utf8mb4;
```



##### 2.3 redis安装

```
sudo apt-get install redis-server
```

注意，redis安装完成以后，要观察redis是否启动了，如果没有启动，则参考之前redis笔记，启动redis。

```
# 查看是否启动redis-server，一般是没启动
# 原因是现在的云服务器基本都默认给redis配置一个IPV6的绑定地址。而我们大部分人的服务器是没使用IPV6的
ps -aux | grep redis

# 如果没有启动，则运行以下命令，再查看是否启动成功，再不行，则查看下面 注意事项
redis-server /etc/redis/redis.conf
```



###### 注意事项

1. 阿里云服务器，需要在云服务器控制台中设置安全组，必须开放redis的6379端口

- 进入控制台,查看实例

  ![1559489486486](assets/1559489486486.png)

- 给安全组配置规则，添加6379端口(一并可以检查是否开放了5000，80，3306等端口)

  ![1559489538202](assets/1559489538202.png)

  ![1559489599224](assets/1559489599224.png)

  ![1559489693057](assets/1559489693057.png)

  ![1559495442142](assets/1559495442142.png)

2. 部分服务器是不支持IPV6的，所以如果启动不了redis可以通过以下命令查看错误日志：

```
cat /var/log/redis/redis-server.log
```

如果日志中出现如下错误：

```
Creating Server TCP listening socket ::1:6379: bind: Cannot assign requested address
```

![1559489815280](assets/1559489815280.png)

::1是一个IPV6的地址，需要在redis配置文件中，找到 bind 127.0.0.1 ::1，把::1移除

![1559489886332](assets/1559489886332.png)

```shell
vim /etc/redis/redis.conf
```

修改完成，:wq退出以后，重启redis即可。

```shell
redis-server /etc/redis/redis.conf
```



##### 2.4 安装虚拟环境

默认情况下ubuntu18.04版本中已经内置了Python3.6.7了。但是没有内置pip。所以先安装pip。

```
sudo apt install python3-pip
pip3 install virtualenv
pip3 install virtualenvwrapper
```

安装完成了以后，接下来需要配置系统环境变量

```bash
mkdir $HOME/.virtualenvs
```

执行命令，打开并编辑 ~/.bashrc

```shell
vim  ~/.bashrc
```

文件末尾添加以下几行代码(注意最后一句命令，和我们本地的有所不同)，:wq 保存退出。

```shell
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

刷新配置文件

```shell
source ~/.bashrc
```



##### 2.5 虚拟环境中安装基本模块

创建虚拟环境

```shell
mkvirtualenv moguapp -p python3
```

安装依赖模块

```python
pip install flask==1.0.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pymysql==0.9.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install redis==3.2.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask-sqlalchemy==2.4.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask-mysqldb==0.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask-session==0.3.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask-script==2.0.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask-migrate==2.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```



我们把项目搭建在/home/mogu目录下

```shell
cd /home
mkdir mogu
cd mogu
# 创建flask项目启动文件manage.py
vim manage.py
```

manage.py文件代码：

```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
      return 'hello,moluo~'

    if __name__ == '__main__':
      app.run()
```

在终端下使用python manage.py运行测试服务器

```shell
python manage.py
```

效果：

![1559495592255](assets/1559495592255.png)

前面我们已经在云服务器控制台的网络安全组中添加5000端口，所以可以直接通过浏览器进行访问。

![1559495648250](assets/1559495648250.png)

到码云上面，创建一个git仓库，把服务器代码上传到码云

```
git config --global user.name "mooluo"
git config --global user.email "649641514@qq.com"
git init
git add .
git commit -m "创建manage.py启动文件"
git remote add origin https://gitee.com/mooluo/mogu.git
git push -u origin master
```





## 服务端项目初始化

### 目录结构

```shell
mogu/
├─ logs/                   # 日志文件存储目录
├─ apps/                   # 项目主要逻辑业务代码保存目录
│  ├─ __init__.py          # 项目初始化文件
│  ├─ modules/             # 保存项目中所有api模块的存储目录
│  │  ├─ common/           # 公共api接口目录
│  │  │  ├─ __init__.py    # 公共api接口的初始化文件
│  │  │  ├─ models.py      # 公共api接口的模型文件
│  │  │  └─ api.py         # 公共api接口代码文件
│  │  └─ __init__.py
|  ├─ utils/               # 项目自定义封装工具包目录
|  ├─ libs/                # 项目第三方工具包目录
|  ├─ settings/            # 项目配置存储目录
│  │  ├─ dev.py            # 开发阶段的配置文件
│  │  ├─ prod.py           # 生产阶段的配置文件
│  │  └─ __init__.py
│  └─ statics/             # 保存项目中所有的静态资源文件[img/css/js]
└── manage.py              # 项目的终端管理脚本文件
```



### Config项目配置

在`settings/__init__.py` 编写基本配置代码

```python
import os
import sys
from redis import Redis
from apps.utils.helper import get_redis_connection
class Config(object):
	"""项目公共配送至"""
	# 把主应用目录设置为 默认导包路径
	BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
	sys.path.insert(0, BASE_DIR )
	# 把蓝图存储设置默认导包路径
	sys.path.insert(0, os.path.join(BASE_DIR, "modules") )

	# 调试模式
	DEBUG = True

	# 设置密钥，可以通过 base64.b64encode(os.urandom(48)) 来生成一个指定长度的随机字符串
	SECRET_KEY = "T1vEjTCjkGon5vU8C6Xq3ujNSQgHQje"

	# 配置日志
	LOG_LEVEL = "DEBUG"
	LOG_FILE_PATH = os.path.join( os.path.dirname( BASE_DIR ), "logs/mogu.log" )
	LOG_FILE_SIZE = 500 * 1024* 1024
	LOG_FILE_NUMBER = 10

	# 数据库的配置信息
	SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/moguapp?charset=utf8"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = False

	# redis配置
	REDIS = {
		'default': {
			'host': '127.0.0.1',  # 项目上线以后，这个地址就会被替换成真实IP地址，mysql也是
			'port': 6379,
			'db': 0
		},
		'session': {
			'host': '127.0.0.1',  # 项目上线以后，这个地址就会被替换成真实IP地址，mysql也是
			'port': 6379,
			'db': 1
		}
	}


	# session 配置
	SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
	SESSION_USE_SIGNER = True  # session_id 进行加密签名处理
	SESSION_REDIS = get_redis_connection( REDIS.get("session") )
	PERMANENT_SESSION_LIFETIME = 24 * 60 * 60  # session 的有效期，单位是秒
```

`settings/dev.py`编写开发环境的配置信息，代码:

```python
from . import Config
class DevConfig(Config):
  """开发模式下的配置"""
  DEBUG = True
  SQLALCHEMY_ECHO = True
```

`settings/prop.py`编写生产环境的配置信息，代码:

```python
from . import Config
class ProdConfig(Config):
    """生产模式下的配置"""
    DEBUG = False
    LOG_LEVEL = "INFO"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
```



### 配置项目日志

把日志设置封装成一个函数`setup_log`，保存到`utils/log.py`文件中

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_log(Config):
    # 设置日志的记录等级
    logging.basicConfig(level=Config.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(
        Config.LOG_FILE_PATH,
        maxBytes=Config.LOG_FILE_SIZE, backupCount=Config.LOG_FILE_NUMBER)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaskapp使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
```



### 项目初始化代码抽取

在`apps/__init__.py`文件中，创建flask应用并加载配置

```python
# coding=utf-8
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from .settings.dev import DevConfig
from .settings.prod import ProdConfig
from .utils.log import setup_log
from .utils.helper import get_redis_connection
from flask_script import Manager,Command
from flask_migrate import Migrate, MigrateCommand

config = {
	"dev": DevConfig,
	"prop": ProdConfig,
}

# 创建数据库链接对象
db = SQLAlchemy()

def init_app(config_name):
	"""项目的初始化功能"""
	app = Flask(__name__)

	# 终端脚本工具
	app.manager = Manager(app)

	# 启用数据迁移工具
	Migrate(app, db)
	# 添加数据迁移的命令到终端脚本工具中
	app.manager.add_command('db', MigrateCommand)

	# 设置配置类
	Config = config.get(config_name)

	# 加载配置
	app.config.from_object(Config)

	# redis的链接初始化
	app.redis = get_redis_connection(Config.REDIS.get("default") )

	# 开启session功能
	Session(app)

	# 配置数据库链接
	db.init_app(app)

	# 启动日志
	setup_log(Config)

	return app
```



### 配置项目启动文件

manage.py启动文件中，加载app初始化工厂函数，并使用flask-script启动项目

`manage.py`，代码：

```python
from apps import init_app

app = init_app("dev")

@app.route("/")
def index():
    return 'hello,moluo~'

if __name__ == '__main__':
    app.manager.run()
```



在终端重新使用manage.py启动项目

```shell
python manage.py runserver --host=0.0.0.0 --port=5000
```



## 基于Flask-JSONRPC提供RPC接⼝

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

把jsonrpc模块的初始化代码抽离到app对象初始化函数init__app中。

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



modules/common/api.py，代码：

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
from apps.modules.common import api

@app.route('/')
def index():
  return 'hello,moluo~'

if __name__ == '__main__':
    manager.run()
```

重新启动项目，使用postman进行还是原来的结果，则表示调整成功，后面的开发中，我们只需要不断增加对应的接口即可。



### 使用jsonrpc接受客户端请求的参数

服务器提供rpc接口方法：

```python
from apps import jsonrpc

@jsonrpc.method("模块名.方法名(username=String, password=String)")
def 方法名(username,password):
    return u"账号：%s，密码：%s" % (username,password)
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
jsonrpc = JSONRPC(service_url="/api/v1", site=JSONRPCSite(), enable_web_browsable_api=True)
jsonrpc_v2 = JSONRPC(service_url="/api/v2", site=JSONRPCSite(), enable_web_browsable_api=True)


def init_app(config_name):
  
  。。。。

  # 启动日志
  init_log(Config)

  # 把jsonrpc注入到app实例对象中
  jsonrpc.init_app(app)
  jsonrpc2.init_app(app)

  return app

```

模块目录modules/common/api.py，代码：

```python
from apps import jsonrpc,jsonrpc2

@jsonrpc.method("Common.add(username=String,age=Number,sex=Boolean,lve=Array,son=Object)")
def add_v1(username,age,sex,lve,son):
  return "username=%s,age=%s,sex=%s,lve=%s,son=%s" % (username,age,sex,lve,son)

@jsonrpc2.method("Common.add(username=String,age=Number,sex=Boolean,lve=Array,son=Object)")
def add_v2(username,age,sex,lve,son):
  return u"账号=%s,年龄=%s,性别=%s,爱好=%s,后代=%s" % (username,age,sex,lve,son)

```

最终效果：

![1559535070805](assets/1559535070805.png)



![1559535083598](assets/1559535083598.png)







# APICloud的基本入门

## 目录结构

```python
.
|-- config.xml         # app核心配置文件
|-- css/               # 公共css存储目录
|   |-- api.css
|   `-- style.css
|-- feature            # 启动画面图片
|-- html/              # 页面/窗口的文件存储目录
|-- icon               # 手机应用图标
|-- image/             # 静态图片存储目录
|-- index.html
|-- launch             # 启动画面图片
|-- res                # 除了图片以外的其他文件
|-- script/            # javascript文件存储目录
|   `-- api.js
`-- wgt                # app模块目录
```

### 配置文件

```python
widget id="A12345678901"  version="0.0.1">
    <name></name>
    <description></description>
    <author email="developer@apicloud.com" href="//www.apicloud.com">
        
    </author>
    <content src="index.html" />
    <access origin="*" />
    <preference name="app偏好设置" value="#FFF" />
    <permission name="app权限设置" />
    <feature name="第三方模块相关配置">
        <param name="urlScheme" value="wx7779c7c063a9d4d9" />
    </feature>
</widget>
```

| 元素名      | 描述                                                         | 备注 |
| ----------- | ------------------------------------------------------------ | ---- |
| name        | Widget的名称。如：QQ、新浪微博、微信等                       | 必选 |
| description | Widget的简单描述信息                                         | 可选 |
| author      | Widget的作者信息                                             | 可选 |
| content     | Widget运行的起始页，支持相对/绝对路径                        | 必选 |
| access      | 在哪些页面里面可以访问APICloud的扩展API。一般配置“*”，代表所有页面都允许访问 | 可选 |
| preference  | 偏好设置。配置Widget的一些运行时属性，如：页面是否支持弹动效果、窗口默认背景、页面是否显示滚动条等。该配置可在APICloud Studio的GUI界面中选择并使用。详细请参考[Preference Guide](https://docs.apicloud.com/Dev-Guide/app-config-manual#1) | 可选 |
| permission  | 权限配置。通过此配置向系统声明Widget所用到的系统权限。如：直接拨打电话、直接发送短信、发起定位等。该配置可在APICloud Studio的GUI界面中选择并使用。详细请参考[Platform Permission](https://docs.apicloud.com/Dev-Guide/app-config-manual#2) | 必选 |
| feature     | 功能配置。通过此配置，向系统声明需要使用哪些功能，以及需要传递给该功能的数据。如：使用新浪微博、使用微信分享等。该配置可在APICloud Studio的GUI界面中选择并使用。详细请参考[Feature Guide](https://docs.apicloud.com/Dev-Guide/app-config-manual#3) | 可选 |
| font        | 字体配置。通过此配置，将自定义字体加入到应用中，使其可以在前端页面使用该字体 | 可选 |





# 欢迎页面

欢迎页面是用户打开APP看到的第一个页面，我们要实现欢迎页面，首先要弄清楚APICloud开发过程中的几个关于页面的概念：

```
window       APP的窗口
Frame        窗口里面的框架页面
FrameGroup   框架页面的组合
```



```javascript
api.openWin({
    name: 'page1',        # window名字
    url: './page1.html',  # 页面地址，可以为本地文件路径，支持相对路径和绝对路径
    pageParam: {          # 页面参数，新页面中可以通过 api.pageParam 获取
        name: 'test'
    }
});
```


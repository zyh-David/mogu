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
		降低开发成本和技术成本，降低维护成本和开发周期
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
	<meta http-equiv="Refresh" content="5;url=http://www.baidu.com.cn" />
</head>
```



### 视口（Viewport）

视口是一个相对比较复杂的概念，所以我们可以简单的理解为，viewport就是用户看手机页面时的<mark>可视区域</mark>，相当于桌面浏览器的窗口。在桌面浏览器中，viewport 就是浏览器窗口的宽度高度。但在移动端设备上就有点太窄了。

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



下载<mark>稳定版</mark>即可，安装步骤省略。安装完成以后，使用USB连接线或者wifi，连接电脑和手机。

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
4. 有多余的软件阻止了共屏，360安全卫士呀，防火墙呀，电脑管家呀，杀毒软件呀，谷歌浏览器的都关了吧。
```

![1559242732629](assets/1559242732629.png)



最终共屏效果：

![1559243711305](assets/1559243711305.png)





# 项目搭建

## 移动端项目搭建

在打开的

ud编辑器中点选<mark>新建项目</mark>即可。

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

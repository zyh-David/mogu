

## 获取文章列表页的API接口

接下来，我们需要把列表页展示出来，所以在config.xml中修改APP的默认首页

```html
<content src="html/news.html" />
```

### 展示文章列表数据

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>全部内容-蘑菇网-你的专业导购</title>
    <meta name="Keywords" content="蘑菇网,女装,时尚潮流,网上购物" />
    <meta name="Description" content="蘑菇网-成立于2016年底，横空而降的专业女装导购网站，您的信赖，是我们从事的唯一标准。" />
    <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
    <!-- Mobile Devices Support @begin -->
    <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
    <meta content="no-cache,must-revalidate" http-equiv="Cache-Control">
    <meta content="no-cache" http-equiv="pragma">
    <meta content="0" http-equiv="expires">
    <meta content="telephone=no, address=no" name="format-detection">
    <meta name="apple-mobile-web-app-capable" content="yes" /> <!-- apple devices fullscreen -->
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <!-- Mobile Devices Support @end -->
    <link href="../css/index.css" rel="stylesheet" />
    <link href="../css/common.css" rel="stylesheet" />
    <script src="../script/jquery-1.9.1.min.js"></script>
    <script src="../script/main.js"></script>
    <script src="../script/jquery.rotate.min.js"></script>
    <script src="../script/api.js"></script>
    <script src="../script/settings.js"></script>
    <script src="../script/vue.js"></script>
    <script src="../script/axios.js"></script>
</head>

<body>
<div class="main" id="app">
    <!--头部-->
    <div class="header" id="bktop">
      <div class="logo"><a href=""><img :src="siteconfig.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
    <ul class="xla">
          <li v-for="top in nav_list">
              <a class="dianj dj1" href="javascript:;"><font>{{top.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
              <div class="zilan">
                <a v-for="son in top.children_list" href="">{{son.name}}</a>
              </div>
          </li>
        </ul>
      </div>
      <div class="clearBoth"></div>
  </div>  <!--资讯列表-->
    <div class="newsban">首页 > 潮流资讯 > 全部内容</div>
    <table class="newwclass">
        <tr class="juzhon">
            <td><a class="on"href="">全部内容</a></td>
            <td v-for="category in category_list"><a href="">{{category.name}}</a></td>
        </tr>
    </table>
    <div class="news about">
        <!--资讯列表-->
        <div class="newslist">
          <div class="qtao" v-for="news in paginate.items">
            <div class="mg">
                <div class="mgl"><img :src="news.image_url" width="100%"/></div>
                <div class="mgr">
                    <h3>{{news.title}}</h3>
                    <div class="what">
                        <div class="time">
                            <div class="tub"><img src="../image/time.gif" /></div>
                            <div class="shij">{{news.create_time|dateFormat}}</div>
                            <div class="clearBoth"></div>
                        </div>
                        <div class="time hit">
                            <div class="tub"><img src="../image/hit.gif" /></div>
                            <div class="shij">{{news.read_count}}</div>
                            <div class="clearBoth"></div>
                        </div>
                        <div class="clearBoth"></div>
                    </div>
                    <div class="jianj">{{news.descript}}</div>
                    <div class="ydu">
                        <div class="anniu"><a href=""><img src="../image/ydu.gif" /></a></div>
                        <div class="clearBoth"></div>
                    </div>
                </div>
                <div class="clearBoth"></div>
            </div>
            </div>
        </div>
    </div>
    <!--分页-->
    <table class="page">
        <tr class="juzhon">
            <td v-if="paginate.has_prev" ><a href=""><img src="../image/first.gif" /></a></td>
            <td v-if="paginate.has_prev" ><a href=""><img src="../image/pre.gif" /></a></td>
            <td v-if="paginate.has_prev" ><a href="">{{paginate.page-1}}</a></td>
            <td><a class="on">{{paginate.page}}</a></td>
            <td v-if="paginate.has_next" ><a href="">{{paginate.page+1}}</a></td>
            <td v-if="paginate.has_next" ><a href=""><img src="../image/next.gif" /></a></td>
            <td v-if="paginate.has_next" ><a href=""><img src="../image/last.gif" /></a></td>
        </tr>
    </table>
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
    </div></div>
</body>

<script type="text/javascript">
vm = new Vue({
  el:"#app",
  data:{
      siteconfig:{},     // 站点配置
      category_list:[],  // 文章分类
      nav_list:[      // 导航菜单
        {children_list:[]},
        {children_list:[]},
        {children_list:[]},
      ],
      paginate:{
        page: 1,
        categoty: 0,
        items:[],  // 当前页面的数据项
      },   // 分页器
  },
  created(){
    this.get_site_config();
    this.get_nav_list();
    this.get_news_category();
    this.get_list_news();
  },
  methods:{
    // 站点配置
    get_site_config(){
       axios.post(settings.API,{
          "jsonrpc": "2.0",
          "id": 188,
          "method": "Common.siteconfig",
          "params": {}
        }).then(response=>{
          this.siteconfig = response.data.result;
        }).catch(error=>{
          alert( JSON.stringify(error.response) );
        })
    },
    // 文章分类
    get_news_category(){
      axios.post(settings.API,{
          "jsonrpc": "2.0",
          "method" : "News.news_categoty",
          "params" : {},
          "id"     : 1
      }).then(response=>{
        this.category_list = response.data.result;
      }).catch(error=>{
        alert( JSON.stringify(error.response) );
      })
    },
    // 获取导航菜单
    get_nav_list(){
      axios.post(settings.API,{
          "jsonrpc": "2.0",
          "method" : "Common.nav",
          "params" : {},
          "id"     : 1
      }).then(response=>{
        this.nav_list = response.data.result;
      }).catch(error=>{
        alert( JSON.stringify(error.response) );
      })
    },
    // 分页展示文章列表
    get_list_news(){
      axios.post(settings.API,{
          "jsonrpc": "2.0",
          "method" : "News.list_news",
          "params" : {"page":1},
          "id"     : 1
      }).then(response=>{
        this.paginate = response.data.result;
      }).catch(error=>{
        alert( JSON.stringify(error.response) );
      })
    },
  },
  filters:{
    dateFormat(time){
      return new Date(time).toLocaleDateString().replace("/","-").replace("/","-")
    }
  }
})
</script>
</html>
```



### 实现点击分页或者分类，切换数据

APP文章列表页页面代码：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>全部内容-蘑菇网-你的专业导购</title>
    <meta name="Keywords" content="蘑菇网,女装,时尚潮流,网上购物" />
    <meta name="Description" content="蘑菇网-成立于2016年底，横空而降的专业女装导购网站，您的信赖，是我们从事的唯一标准。" />
    <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
    <!-- Mobile Devices Support @begin -->
    <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
    <meta content="no-cache,must-revalidate" http-equiv="Cache-Control">
    <meta content="no-cache" http-equiv="pragma">
    <meta content="0" http-equiv="expires">
    <meta content="telephone=no, address=no" name="format-detection">
    <meta name="apple-mobile-web-app-capable" content="yes" /> <!-- apple devices fullscreen -->
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <!-- Mobile Devices Support @end -->
    <link href="../css/index.css" rel="stylesheet" />
    <link href="../css/common.css" rel="stylesheet" />
    <script src="../script/jquery-1.9.1.min.js"></script>
    <script src="../script/main.js"></script>
    <script src="../script/jquery.rotate.min.js"></script>
    <script src="../script/api.js"></script>
    <script src="../script/settings.js"></script>
    <script src="../script/vue.js"></script>
    <script src="../script/axios.js"></script>
</head>

<body>
<div class="main" id="app">
    <!--头部-->
    <div class="header" id="bktop">
      <div class="logo"><a href=""><img :src="siteconfig.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
    <ul class="xla">
          <li v-for="top in nav_list">
              <a class="dianj dj1" href="javascript:;"><font>{{top.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
              <div class="zilan">
                <a v-for="son in top.children_list" href="">{{son.name}}</a>
              </div>
          </li>
        </ul>
      </div>
      <div class="clearBoth"></div>
  </div>  <!--资讯列表-->
    <div class="newsban">首页 > 潮流资讯 > {{current_category}}</div>
    <table class="newwclass">
        <tr class="juzhon">
            <td><a :class="paginate.category==0?'on':''" @click="paginate.category=0;current_category='全部内容'">全部内容</a></td>
            <td v-for="category in category_list"><a :class="paginate.category==category.id?'on':''" @click="paginate.category=category.id;current_category=category.name">{{category.name}}</a></td>
        </tr>
    </table>
    <div class="news about">
        <!--资讯列表-->
        <div class="newslist">
          <div class="qtao" v-for="news in paginate.items">
            <div class="mg">
                <div class="mgl"><img :src="news.image_url" width="100%"/></div>
                <div class="mgr">
                    <h3>{{news.title}}</h3>
                    <div class="what">
                        <div class="time">
                            <div class="tub"><img src="../image/time.gif" /></div>
                            <div class="shij">{{news.create_time|dateFormat}}</div>
                            <div class="clearBoth"></div>
                        </div>
                        <div class="time hit">
                            <div class="tub"><img src="../image/hit.gif" /></div>
                            <div class="shij">{{news.read_count}}</div>
                            <div class="clearBoth"></div>
                        </div>
                        <div class="clearBoth"></div>
                    </div>
                    <div class="jianj">{{news.descript}}</div>
                    <div class="ydu">
                        <div class="anniu"><a href=""><img src="../image/ydu.gif" /></a></div>
                        <div class="clearBoth"></div>
                    </div>
                </div>
                <div class="clearBoth"></div>
            </div>
            </div>
        </div>
    </div>
    <!--分页-->
    <table class="page">
        <tr class="juzhon">
            <td v-if="paginate.has_prev && paginate.page>1" ><a @click="paginate.page=1"><img src="../image/first.gif" /></a></td>
            <td v-if="paginate.has_prev && paginate.page>1" ><a @click="paginate.page-=1"><img src="../image/pre.gif" /></a></td>
            <td v-if="paginate.has_prev && paginate.page>1" ><a @click="paginate.page-=1">{{paginate.page-1}}</a></td>
            <td><a class="on">{{paginate.page}}</a></td>
            <td v-if="paginate.has_next && paginate.page < paginate.pages" ><a @click="paginate.page+=1">{{paginate.page+1}}</a></td>
            <td v-if="paginate.has_next && paginate.page < paginate.pages" ><a @click="paginate.page+=1"><img src="../image/next.gif" /></a></td>
            <td v-if="paginate.has_next && paginate.page < paginate.pages" ><a @click="paginate.page=paginate.pages"><img src="../image/last.gif" /></a></td>
        </tr>
    </table>
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
    </div></div>
</body>

<script type="text/javascript">
vm = new Vue({
  el:"#app",
  data:{
      current_category: "全部内容",
      siteconfig:{},     // 站点配置
      category_list:[],  // 文章分类
      nav_list:[      // 导航菜单
        {children_list:[]},
        {children_list:[]},
        {children_list:[]},
      ],
      paginate:{
        page: 1,      // 当前页
        per_page: 2,  // 当前页数据量
        category: 0, // 当前分类
        items:[],    // 当前页面的数据项
      },   // 分页器
      myfilter:{}    // 获取分页的过滤条件
  },
  watch:{
    "paginate.page": function(){
       this.get_list_news();
    },
    "paginate.category": function(){
       this.paginate.page = 1;
       this.get_list_news();
    },
  },
  created(){
    this.get_site_config();
    this.get_nav_list();
    this.get_news_category();
    this.get_list_news();
  },
  methods:{
    // 站点配置
    get_site_config(){
       axios.post(settings.API,{
          "jsonrpc": "2.0",
          "id": 188,
          "method": "Common.siteconfig",
          "params": {}
        }).then(response=>{
          this.siteconfig = response.data.result;
        }).catch(error=>{
          alert( JSON.stringify(error.response) );
        })
    },
    // 文章分类
    get_news_category(){
      axios.post(settings.API,{
          "jsonrpc": "2.0",
          "method" : "News.news_categoty",
          "params" : {},
          "id"     : 1
      }).then(response=>{
        this.category_list = response.data.result;
      }).catch(error=>{
        alert( JSON.stringify(error.response) );
      })
    },
    // 获取导航菜单
    get_nav_list(){
      axios.post(settings.API,{
          "jsonrpc": "2.0",
          "method" : "Common.nav",
          "params" : {},
          "id"     : 1
      }).then(response=>{
        this.nav_list = response.data.result;
      }).catch(error=>{
        alert( JSON.stringify(error.response) );
      })
    },
    // 分页展示文章列表
    get_list_news(){
      this.myfilter = {
        "per_page": this.paginate.per_page,
      }

      if( this.paginate.category > 0 ){
        this.myfilter.category = this.paginate.category;
      }

      if( this.paginate.page > 1 ){
        this.myfilter.page = this.paginate.page;
      }
      axios.post(settings.API,{
          "jsonrpc": "2.0",
          "method" : "News.list_news",
          "params" : this.myfilter,
          "id"     : 1
      }).then(response=>{
        this.paginate = response.data.result;
      }).catch(error=>{
        alert( JSON.stringify(error.response) );
      })
    },
  },
  filters:{
    dateFormat(time){
      return new Date(time).toLocaleDateString().replace("/","-").replace("/","-")
    }
  }
})
</script>

</html>
```



## 获取文章详情页的API接口

接下来，我们需要把详情页展示出来，所以在config.xml中修改APP的默认首页

```html
<content src="html/news_detail.html" />
```

展示文章详情数据

```html

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>蘑菇街</title>
    <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
    <!-- Mobile Devices Support @begin -->
    <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
    <meta content="no-cache,must-revalidate" http-equiv="Cache-Control">
    <meta content="no-cache" http-equiv="pragma">
    <meta content="0" http-equiv="expires">
    <meta content="telephone=no, address=no" name="format-detection">
    <!-- Mobile Devices Support @end -->
    <link href="../css/index.css" rel="stylesheet" />
    <link href="../css/common.css" rel="stylesheet" />
    <script src="../script/jquery-1.9.1.min.js"></script>
    <script src="../script/main.js"></script>
    <script src="../script/jquery.rotate.min.js"></script>
    <script src="../script/api.js"></script>
    <script src="../script/settings.js"></script>
    <script src="../script/vue.js"></script>
    <script src="../script/axios.js"></script>
    <script src="../script/rpc.js"></script>
    <style>
    .is_show_more{height: 2000px;overflow: hidden;display: block;}
    .isnot_need{display: none;}
    </style>
</head>

<body>
<div class="main" id="app">
    <!--头部-->
    <div class="header" id="bktop">
      <div class="logo"><a href=""><img :src="site_config.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
          <ul class="xla">
              <li :key="key" v-for="nav,key in nav_list">
                <a class="dianj dj1" :href="nav.link"><font>{{nav.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
                <div class="zilan" :key="key" v-for="son,key in nav.children_list">
                  <a :href="son.link">{{son.name}}</a>
                </div>
              </li>
           </ul>
      </div>
      <div class="clearBoth"></div>
    </div>
    <!--关于我们内容-->
    <div class="newsban"><a style="color:#ccc" href="">首页</a> > <a style="color:#ccc" href="">{{news.category_name}}</a> > {{news.title}}</div>
    <div class="newbt">{{news.title}}</div>
    <div class="about">
        <div class="content2">
            <table class="what">
                <tr class="time">
                    <td class="tub"><img src="../image/time.gif" /></td>
                    <td class="shij">{{news.created_time|format}}</td>
                    <td class="clearBoth"></td>
                </tr>
                <tr class="time hit">
                    <td class="tub"><img src="../image/hit.gif" /></td>
                    <td class="shij">{{news.read_count}}</td>
                    <td class="clearBoth"></td>
                </tr>
                <td class="clearBoth"></td>
            </table>
            <!--编辑内容-->
            <div class='is_show_more white'>
              {{news.content}}
            </div>
            <div class="more"><img src="../image/more.gif" /></div>
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
        <div class="bottom-bot">{{site_config.copyright}}</div>
    </div>
</div>
<script>
var vm = new Vue({
  el:"#app",
  data:{
    site_config: {},
    nav_list: [],
    news:{},
  },
  created(){
    this.get_site_config();
    this.get_nav_list();
    this.get_news();
  },
  filters:{
    format(date_str){
      date_obj = new Date(date_str);
      let year = date_obj.getFullYear();
      let month = date_obj.getMonth()+1;
      let date = date_obj.getDate();
      month = month<10?'0'+month:month;
      date = date<10?'0'+date:date;
      return `${year}-${month}-${date}`;
    }
  },
  methods:{
    get_site_config(){
      // 获取站点配置
      rpc(settings.API,"Home.site_config",{},result=>{
        this.site_config = result;
      });
    },
    get_nav_list(){
      // 导航菜单
      rpc(settings.API,"Home.nav",{},result=>{
        this.nav_list = result;
      });
    },
    get_news(){
      // 获取文章列表
      let filters = {};
      filters.id = 3;
      rpc(settings.API,"News.news",filters,result=>{
        this.news = result;
      });
    },
  }
});

$('.more').click(function(){
    $('.is_show_more').toggleClass('is_show_more');
    $(this).addClass('isnot_need');
});

</script>
</body>
</html>
```



## 获取商品列表页的API接口

接下来，我们需要把列表页展示出来，所以在config.xml中修改APP的默认首页

```html
<content src="html/products.html" />
```

### 展示商品列表数据

APP商品列表页页面代码：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>蘑菇街</title>
  <meta name="Keywords" content="" />
  <meta name="Description" content="" />
  <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
  <!-- Mobile Devices Support @begin -->
  <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
  <meta content="no-cache,must-revalidate" http-equiv="Cache-Control">
  <meta content="no-cache" http-equiv="pragma">
  <meta content="0" http-equiv="expires">
  <meta content="telephone=no, address=no" name="format-detection">
  <meta name="apple-mobile-web-app-capable" content="yes" /> <!-- apple devices fullscreen -->
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <!-- Mobile Devices Support @end -->
  <link href="../css/index.css" rel="stylesheet" />
  <link href="../css/common.css" rel="stylesheet" />
  <script src="../script/jquery-1.9.1.min.js"></script>
  <script src="../script/jquery.easing.min.js"></script>
  <script src="../script/main.js"></script>
  <script src="../script/jquery.rotate.min.js"></script>
  <script src="../script/api.js"></script>
  <script src="../script/settings.js"></script>
  <script src="../script/vue.js"></script>
  <script src="../script/axios.js"></script>
  <script src="../script/rpc.js"></script>
</head>

<body>
<div class="main" id="app">
	<!--头部-->
  <div class="header" id="bktop">
    <div class="logo"><a href=""><img :src="site_config.logo" /></a></div>
    <div class="banner">
        <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
        <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
        <ul class="xla">
            <li :key="key" v-for="nav,key in nav_list">
              <a class="dianj dj1" :href="nav.link"><font>{{nav.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
              <div class="zilan" :key="key" v-for="son,key in nav.children_list">
                <a :href="son.link">{{son.name}}</a>
              </div>
            </li>
         </ul>
    </div>
    <div class="clearBoth"></div>
  </div>
	<!--资讯列表-->
	<div class="newsban">首页 > 产品分类 > {{current_category_text}}</div>
	<table class="newwclass">
    <tr class="juzhon">
        <td><a :class="filters.category==0?'on':''" @click="filters.category=0;current_category_text='全部商品'">全部商品</a></td>
        <td v-for="category in goods_category"><a :class="filters.category==category.id?'on':''" @click="filters.category=category.id;current_category_text=category.name;">{{category.name}}</a></td>
    </tr>
	</table>
	<div class="xlan"></div>
	<div class="case_list">
		<div class="case_list_body">
			<ul>
				<!--第二个加属性noright-->
				<li :class="key%2==0?'yyu':'casela'" v-for="goods,key in goods_list.items">
					<a href="#">
						<div class="case_list_body_pic">
							<img :src="goods.image_url">
						</div>
					</a>
					<div class="case_list_info">
						<p class="cast_list_tit"><a href="product.html">{{goods.title}}</a></p>
					</div>
				</li>
				<div class="clearBoth">
			</ul>
		</div>
	</div>
  <!--分页-->
  <table class="page" v-if="goods_list.pages>1">
      <tr class="juzhon">
          <td v-if="goods_list.has_prev"><a @click="filters.page=1"><img src="../image/first.gif" /></a></td>
          <td v-if="goods_list.has_prev"><a @click="filters.page=goods_list.prev_num"><img src="../image/pre.gif" /></a></td>
          <td v-if="goods_list.has_prev"><a @click="filters.page=goods_list.prev_num">{{goods_list.prev_num}}</a></td>
          <td><a :class="filters.page==goods_list.page?'on':''">{{goods_list.page}}</a></td>
          <td v-if="goods_list.has_next"><a @click="filters.page=goods_list.next_num">{{goods_list.next_num}}</a></td>
          <td v-if="goods_list.has_next"><a @click="filters.page=goods_list.next_num"><img src="../image/next.gif" /></a></td>
          <td v-if="goods_list.has_next"><a @click="filters.page=goods_list.pages"><img src="../image/last.gif" /></a></td>
      </tr>
  </table>
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
      <div class="bottom-bot">{{site_config.copyright}}</div>
  </div>
</div>
<script>
var vm = new Vue({
  el:"#app",
  data:{
    site_config: {},
    nav_list: [],
    goods_list: [],
    goods_category: [],
    current_category_text:"全部商品",
    filters:{
      category: 0,
      page: 1,  // 当前页码
      size: 2,  // 单页数据量
    }
  },
  watch:{
    "filters.page":function(){
      this.get_goods_list();
    },
    "filters.category":function(){
      this.filters.page = 1;
      this.get_goods_list();
    },
    "filters.size":function(){
      this.filters.page = 1;
      this.get_goods_list();
    }
  },
  created(){
    this.get_site_config();
    this.get_nav_list();
    this.get_goods_category();
    this.get_goods_list();
  },
  filters:{
    format(date_str){
      date_obj = new Date(date_str);
      let year = date_obj.getFullYear();
      let month = date_obj.getMonth()+1;
      let date = date_obj.getDate();
      month = month<10?'0'+month:month;
      date = date<10?'0'+date:date;
      return `${year}-${month}-${date}`;
    }
  },
  methods:{
    get_site_config(){
      // 获取站点配置
      rpc(settings.API,"Home.site_config",{},result=>{
        this.site_config = result;
      });
    },
    get_nav_list(){
      // 导航菜单
      rpc(settings.API,"Home.nav",{},result=>{
        this.nav_list = result;
      });
    },
    get_goods_category(){
      // 获取商品分类
      rpc(settings.API,"Goods.goods_category",{},result=>{
        this.goods_category = result;
      });
    },
    get_goods_list(){
      // 获取商品列表
      let filters = {}
      if( this.filters.category > 0 ){
        filters.category = this.filters.category;
      }
      filters.page = this.filters.page;
      filters.size = this.filters.size;

      rpc(settings.API,"Goods.list_goods",filters,result=>{
        this.goods_list = result;
      });
    },
  }
});
</script>
</body>

</html>

```



## 获取商品详情页的API接口

接下来，我们需要把详情页展示出来，所以在config.xml中修改APP的默认首页

```html
<content src="html/product.html" />
```

经过查看，我们需要在这个页面中，获取到6个接口数据

```
导航菜单、站点配置、商品图片、商品信息、商品参数、同类热门
```

### 后端分析实现商品详情和商品图片的数据模型

![1568002980503](assets/1568002980503.png)

goods/models.py，代码：

```python
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
```

通过git上传到服务器，并执行数据迁移。

```bash
git pull
python manage.py db migrate -m "新增商品sku和属性图片相关的模型"
python manage.py db upgrade
```

#### 添加sku相关的测试数据

```python
# 关闭外键约束功能
SET foreign_key_checks=0;
truncate `moguapp`.`mogu_goods_type`;
truncate `moguapp`.`mogu_goods_sku`;
truncate `moguapp`.`mogu_goods_attribute`;
truncate `moguapp`.`mogu_goods_attribute_option`;
truncate `moguapp`.`mogu_goods_sku_attribute`;
# 开启外键约束功能
SET foreign_key_checks=1;

# 添加商品类型
INSERT INTO `mogu_goods_type` (`name`,`is_deleted`,`is_show`) values ('衣服',0,1),('手机',0,1),('笔记本',0,1);

# 给所有商品指定商品类型为衣服
update mogu_goods_spu set type_id = 1;

# 添加商品SKU
INSERT INTO `mogu_goods_sku` (`spu_id`,`sale`,`number`,`price`,`is_deleted`,`is_show`) values (1,100,100,100,0,1),(1,100,100,100,0,1),(2,100,100,100,0,1),(2,100,100,100,0,1),(2,100,100,100,0,1),(2,100,100,100,0,1),(3,100,100,100,0,1),(4,100,100,100,0,1),(4,100,100,100,0,1),(4,100,100,100,0,1),(5,100,100,100,0,1),(5,100,100,100,0,1);

# 添加商品属性
INSERT INTO `mogu_goods_attribute` (`type_id`,`name`,`value_type`,`is_deleted`,`is_show`) values (1,'尺码','单选值',0,1),(2,'腰型','单选值',0,1),(1,'袖长','单选值',0,1),(1,'颜色','单选值',0,1),(1,'领型','单选值',0,1);

# 添加商品属性值选项
INSERT INTO `mogu_goods_attribute_option` (`attr_id`,`option`,`is_deleted`,`is_show`) values (1,'S',0,1),(1,'L',0,1),(1,'M',0,1),(1,'XL',0,1),(1,'XXL',0,1),(1,'XXXL',0,1),(2,'高腰',0,1),(2,'中腰',0,1),(2,'低腰',0,1),(3,'短袖',0,1),(3,'长袖',0,1),(3,'中长袖',0,1),(3,'无袖',0,1),(4,'纯色',0,1),(4,'黑紫色',0,1),(4,'白色',0,1),(4,'天蓝色',0,1),(4,'粉色',0,1),(5,'圆领',0,1),(5,'无领',0,1),(5,'V领',0,1);


# 添加具体商品的属性和属性值关系
INSERT INTO `mogu_goods_sku_attribute` (`attr_id`,`value`,`sku_id`,`is_deleted`,`is_show`) values (1,1,1,0,1),(2,7,1,0,1),(3,13,1,0,1),(4,14,1,0,1),(5,21,1,0,1),(1,3,2,0,1),(2,7,2,0,1),(3,13,2,0,1),(4,15,2,0,1),(5,21,2,0,1);

# 增加sku库存的图片信息
INSERT INTO `mogu_goods_image` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `image_url`, `sku_id`) VALUES ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 5),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 5),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 6),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 6),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 6),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8);
```



### 编写商品详情的API接口

服务端提供spu基本商品信息和同类热门商品信息，goods/api.py，代码：

```python
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

```



### APP 展示spu商品基本数据和同类热门商品

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-蘑菇网-你的专业导购</title>
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
  <script src="../script/api.js"></script>
  <script src="../script/settings.js"></script>
  <script src="../script/vue.js"></script>
  <script src="../script/axios.js"></script>
  <script src="../script/rpc.js"></script>
</head>
<body>
<div class="main" id="app">
  <!--头部-->
  <div class="header" id="bktop">
    <div class="logo"><a href=""><img :src="site_config.logo" /></a></div>
    <div class="banner">
        <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
        <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
        <ul class="xla">
            <li :key="key" v-for="nav,key in nav_list">
              <a class="dianj dj1" :href="nav.link"><font>{{nav.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
              <div class="zilan" :key="key" v-for="son,key in nav.children_list">
                <a :href="son.link">{{son.name}}</a>
              </div>
            </li>
         </ul>
    </div>
    <div class="clearBoth"></div>
  </div>
  <!--产品信息-->
  <div class="newsban"><a style="color:#ccc" href="">首页</a> > <a style="color:#ccc" href="">{{goods_spu.category_name}}</a> > {{goods_spu.title}} </div>
  <div id="main">
    <div class="home-device">
      <a class="arrow-left" href="#"></a>
      <a class="arrow-right" href="#"></a>
      <div class="swiper-main">
        <div class="swiper-container swiper1">
          <div class="swiper-wrapper">
            <div class="swiper-slide"><img src="../image/product/pro-2.jpg" width="100%"></div>
            <div class="swiper-slide"><img src="../image/product/pro-1.jpg" width="100%"></div>
            <div class="swiper-slide"><img src="../image/product/pro-3.jpg" width="100%"></div>
            <div class="swiper-slide"><img src="../image/product/pro-2.jpg" width="100%"></div>
            <div class="swiper-slide"><img src="../image/product/pro-1.jpg" width="100%"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="dian"><div class="pagination pagination1"></div></div>
  </div>
  <div class="newbt2">2016冬季新款韩版长款过膝韩国宽松纯色棉衣</div>
  <div class="about">
    <div class="content2">
      <!-- start -->
      <div class="page-btn">
        <span class="swiper-pagination-active">商品详情</span>
        <span>商品参数</span>
        <span>同类热门</span>
      </div>
      <div class="swiper-container swiper2">
        <div class="swiper-wrapper">
          <div class="swiper-slide product-content">
            <p class="image-list-title"><span>商品描述</span></p>
            <div class="product-desc white">
              {{goods_spu.descript}}
            </div>
            <p class="image-list-title"><span>穿着效果</span></p>
            <div class="product-desc white">
              {{goods_spu.effect}}
            </div>
          </div>
          <div class="swiper-slide product-param">
            <table class="parameter-table">
              <tr>
                  <td>尺码: S,L,M</td>
                  <td>裙型: 直筒裙</td>
                  <td>腰型: 中腰</td>
                </tr>
              <tr>
                  <td>材质: 棉</td>
                  <td>颜色: 经典白</td>
                  <td>袖长: 长袖</td>
                </tr>
              <tr>
                  <td>组合形式: 单件</td>
                  <td>风格: 通勤（OL）,韩系</td>
                  <td>裙长: 短裙（76-90cm）</td>
                </tr>
              <tr>
                  <td>版型: 直筒</td>
                  <td>元素: 纯色</td>
                  <td>领型: 圆领</td>
                </tr>
              <tr>
                  <td>图案: 纯色</td>
                  <td>季节: 冬季,季季</td>
                </tr>
            </table>
          </div>
          <div class="swiper-slide">
            <div class="case_list">
              <div class="case_list_body case_list_body2 case_list_body3">
                <ul>
                  <li :class="key%2==0?'yyu':'casela'" v-for="goods,key in hot_goods">
                  <a href="">
                    <div class="case_list_body_pic">
                      <img :src="goods.image_url">
                    </div>
                  </a>
                  <div class="case_list_info">
                    <p class="cast_list_tit"><a href="">{{goods.title}}</a></p>
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
      <div class="bottom-bot">{{site_config.copyright}}</div>
  </div>
</div>
<script>
var vm = new Vue({
  el:"#app",
  data:{
    spu_id: 1,
    site_config: {},
    nav_list: [],
    goods_spu:{},
    hot_goods:[],
  },
  created(){
    this.get_site_config();
    this.get_nav_list();
    this.get_goods_spu();
  },
  filters:{
    format(date_str){
      date_obj = new Date(date_str);
      let year = date_obj.getFullYear();
      let month = date_obj.getMonth()+1;
      let date = date_obj.getDate();
      month = month<10?'0'+month:month;
      date = date<10?'0'+date:date;
      return `${year}-${month}-${date}`;
    }
  },
  methods:{
    get_site_config(){
      // 获取站点配置
      rpc(settings.API,"Home.site_config",{},result=>{
        this.site_config = result;
      });
    },
    get_nav_list(){
      // 导航菜单
      rpc(settings.API,"Home.nav",{},result=>{
        this.nav_list = result;
      });
    },
    get_goods_spu(){
      // 获取商品的spu基本信息
      rpc(settings.API,"Goods.detail_spu_goods",{
        "spu_id": this.spu_id
      },result=>{
        this.goods_spu = result;
        // 继续请求同类热门信息
        this.get_hot_goods();
      });
    },
    get_hot_goods(){
      // 获取同类热门信息
      rpc(settings.API,"Goods.detail_hot_goods",{
        "category": this.goods_spu.category_id
      },result=>{
        this.hot_goods = result;
      });
    }
  }
});
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
</script>
</body>
</html>

```



### sku商品属性展示

把数据库中现有的SKU的商品标题进行修改：

```python
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-1' where id=1;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-2' where id=2;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-3' where id=3;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-4' where id=4;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-5' where id=5;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-6' where id=6;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-7' where id=7;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-8' where id=8;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-9' where id=9;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-10' where id=10;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-11' where id=11;
update `mogu_goods_sku` set title='2016冬季新款韩版长款过膝韩国宽松纯色棉衣-12' where id=12;

update `mogu_goods_sku` set created_time="2019-09-08 12:30:00",updated_time="2019-09-08 12:30:00";
```



在服务端中提供根据spu_id获取当前系列所有库存商品信息，同时提供sku的商品图片信息和sku的商品属性信息。

goods/api.py，代码：

```python
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
```



#### APP获取商品属性API

在商品详情页面中，展示当前sku商品对应的价格！

```python
在商品标题处增加价格内容的显示：
  <div class="newbt2">{{goods.title}} <span class="goods_price">￥40.00</span></div>
  <ul class="sku_list white">
    <li><span>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-1</span></li>
    <li><span>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-2</span></li>
    <li><span>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-3</span></li>
    <li><span>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-4</span></li>
    <li><span>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-5</span></li>
    <li><span>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-6</span></li>
  </ul>
```



当用户选择不同的SKU商品时，发送ajax请求到后端查询数据

```vue
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>2016冬季新款韩版长款过膝韩国宽松纯色棉衣-蘑菇网-你的专业导购</title>
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
  <script src="../script/api.js"></script>
  <script src="../script/settings.js"></script>
  <script src="../script/vue.js"></script>
  <script src="../script/axios.js"></script>
  <script src="../script/rpc.js"></script>
</head>
<body>
<div class="main" id="app">
  <!--头部-->
  <div class="header" id="bktop">
    <div class="logo"><a href=""><img :src="site_config.logo" /></a></div>
    <div class="banner">
        <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
        <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
        <ul class="xla">
            <li :key="key" v-for="nav,key in nav_list">
              <a class="dianj dj1" :href="nav.link"><font>{{nav.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
              <div class="zilan" :key="key" v-for="son,key in nav.children_list">
                <a :href="son.link">{{son.name}}</a>
              </div>
            </li>
         </ul>
    </div>
    <div class="clearBoth"></div>
  </div>
  <!--产品信息-->
  <div class="newsban"><a style="color:#ccc" href="">首页</a> > <a style="color:#ccc" href="">{{goods_spu.category_name}}</a> > {{goods_spu.title}} </div>
  <div id="main">
    <div class="home-device">
      <a class="arrow-left" href="#"></a>
      <a class="arrow-right" href="#"></a>
      <div class="swiper-main">
        <div class="swiper-container swiper1">
          <div class="swiper-wrapper">
            <div v-for="image in goods_sku_image" class="swiper-slide"><img :src="image.image_url" width="100%"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="dian"><div class="pagination pagination1"></div></div>
  </div>
  <div class="newbt2">{{current_sku_goods.title}} <span class="goods_price">￥{{current_sku_goods.sale_price}}</span></div>
  <ul class="sku_list white">
    <li @click="sku_id=goods.id" :class="sku_id===goods.id?'on':''" v-for="goods in goods_sku"><span>{{goods.title}}</span></li>
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
        <div class="swiper-wrapper">
          <div class="swiper-slide product-content">
            <p class="image-list-title"><span>商品描述</span></p>
            <div class="product-desc white">
              {{goods_spu.descript}}
            </div>
            <p class="image-list-title"><span>穿着效果</span></p>
            <div class="product-desc white">
              {{goods_spu.effect}}
            </div>
          </div>
          <div class="swiper-slide product-param">
            <table class="parameter-table">
              <tr v-for="value,key in goods_sku_attr">
                <td>{{key}}: {{value}}</td>
              </tr>
            </table>
          </div>
          <div class="swiper-slide">
            <div class="case_list">
              <div class="case_list_body case_list_body2 case_list_body3">
                <ul>
                  <li :class="key%2==0?'yyu':'casela'" v-for="goods,key in hot_goods">
                  <a href="">
                    <div class="case_list_body_pic">
                      <img :src="goods.image_url">
                    </div>
                  </a>
                  <div class="case_list_info">
                    <p class="cast_list_tit"><a href="">{{goods.title}}</a></p>
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
      <div class="bottom-bot">{{site_config.copyright}}</div>
  </div>
</div>
<script>
var vm = new Vue({
  el:"#app",
  data:{
    spu_id: 1,
    site_config: {},
    nav_list: [],
    goods_spu:{},
    hot_goods:[],
    goods_sku:[],
    current_sku_goods:{}, // 当前显示的sku商品
    sku_id: 0,
    goods_sku_image:[],
    goods_sku_attr:{},
  },
  watch:{
    "sku_id": function(){
      for(let key in this.goods_sku){
        if(this.goods_sku[key].id == this.sku_id){
            this.current_sku_goods = this.goods_sku[key];
        }
      }
      this.get_goods_sku_image();
      this.get_goods_sku_attr();
    }
  },
  created(){
    this.get_site_config();
    this.get_nav_list();
    this.get_goods_spu();
    this.get_goods_sku();
  },
  filters:{
    format(date_str){
      date_obj = new Date(date_str);
      let year = date_obj.getFullYear();
      let month = date_obj.getMonth()+1;
      let date = date_obj.getDate();
      month = month<10?'0'+month:month;
      date = date<10?'0'+date:date;
      return `${year}-${month}-${date}`;
    }
  },
  methods:{
    get_site_config(){
      // 获取站点配置
      rpc(settings.API,"Home.site_config",{},result=>{
        this.site_config = result;
      });
    },
    get_nav_list(){
      // 导航菜单
      rpc(settings.API,"Home.nav",{},result=>{
        this.nav_list = result;
      });
    },
    get_goods_spu(){
      // 获取商品的spu基本信息
      rpc(settings.API,"Goods.detail_spu_goods",{
        "spu_id": this.spu_id
      },result=>{
        this.goods_spu = result;
        // 继续请求同类热门信息
        this.get_hot_goods();
      });
    },
    get_hot_goods(){
      // 获取同类热门信息
      rpc(settings.API,"Goods.detail_hot_goods",{
        "category": this.goods_spu.category_id
      },result=>{
        this.hot_goods = result;
      });
    },
    get_goods_sku(){
      // 获取当前系列的所有库存商品
      rpc(settings.API,"Goods.detail_sku_goods",{
        "spu_id": this.spu_id
      },result=>{
        this.goods_sku = result;
        // 默认第一个商品为当前显示的sku商品信息
        this.sku_id = this.goods_sku[0].id;
      });
    },
    get_goods_sku_image(){
      // 获取当前sku商品的图片
      rpc(settings.API,"Goods.detail_sku_goods_image",{
        "sku_id": this.sku_id
      },result=>{
        this.goods_sku_image = result;
      });
    },
    get_goods_sku_attr(){
      // 获取当前sku商品的属性
      rpc(settings.API,"Goods.detail_sku_goods_attr",{
        "sku_id": this.sku_id
      },result=>{
        this.goods_sku_attr = result;
      });
    }
  }
});

  // 商品图片
  swiper = new Swiper('.swiper1', {
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
</script>
</body>
</html>
```



## 其他杂项

### 页面跳转

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

#### 添加导航测试

```sql
UPDATE `mogu_nav` SET link='./products.html' where id = 6;
UPDATE `mogu_nav` SET link='./products.html' where id = 4;
UPDATE `mogu_nav` SET link='./products.html' where id = 5;

UPDATE `mogu_nav` SET link='./news.html' where parent_id=2;
UPDATE `mogu_nav` SET link='./news_detail.html' where parent_id=3;
```

在页面的头部部分实现页面的跳转.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>蘑菇网-你的专业导购</title>
    <meta name="Keywords" content="蘑菇网,女装,时尚潮流,网上购物" />
    <meta name="Description" content="蘑菇网-成立于2016年底，横空而降的专业女装导购网站，您的信赖，是我们从事的唯一标准。" />
    <meta content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport">
    <!-- Mobile Devices Support @begin -->
    <meta content="application/xhtml+xml;charset=UTF-8" http-equiv="Content-Type">
    <!-- Mobile Devices Support @end -->
    <link href="../css/index.css" rel="stylesheet" />
    <link href="../css/common.css" rel="stylesheet" />
    <link href="../css/swiper-3.4.0.min.css" rel="stylesheet" />
    <script src="../script/jquery-1.9.1.min.js"></script>
    <script src="../script/main.js"></script>
    <script src="../script/jquery.rotate.min.js"></script>
    <script src="../script/jQuery-jcMarquee.js"></script>
    <script src="../script/swiper-3.4.0.min.js"></script>
    <script src="../script/settings.js"></script>
    <script src="../script/rpc.js"></script>
    <script src="../script/api.js"></script>
    <script src="../script/vue.js"></script>
    <script src="../script/axios.js"></script>
</head>

<body>
<div class="main" id="app">
    <!--头部-->
    <div class="header" id="bktop">
      <div class="logo"><a href=""><img :src="site_config.logo" /></a></div>
      <div class="banner">
          <div class="close"><img id="img1" src="../image/banner01.gif" /></div>
          <div class="open hide"><img id="img2" src="../image/banner02.gif" /></div>
          <ul class="xla">
              <li :key="key" v-for="nav,key in nav_list">
                <a class="dianj dj1"><font>{{nav.name}}</font><img id="ig1" src="../image/xiala.gif" /></a>
                <div class="zilan" :key="key" v-for="son,key in nav.children_list">
                  <a @click="jump(son.link)">{{son.name}}</a>
                </div>
              </li>
           </ul>
      </div>
      <div class="clearBoth"></div>
    </div>
      <!--滚动图-->
      <div id="main">
        <div class="home-device">
            <a class="arrow-left" href="#"></a>
            <a class="arrow-right" href="#"></a>
            <div class="swiper-main">
                <div class="swiper-container swiper1">
                    <div class="swiper-wrapper">
                        <div class="swiper-slide" :key="key" v-for="banner,key in banner_list"><a :href="banner.link"><img :src="banner.image_url" width="100%"></a></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="dian"><div class="pagination pagination1"></div></div>
      </div>
    <div class="news">
        <!--滚动公告-->
        <div class="gongao">
            <div class="laba"><img src="../image/gongao.gif" /></div>
            <div class="wenzi" id="mrq">
                <div id="Marquee_x">
                    <ul>
                        <li>
                            <div>{{site_config.phrase}}</div>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="clearBoth"></div>
        </div>
        <!--潮流新品-->
        <h2 class="floor-title">今日"心"品</h2>
        <div class="case_list">
            <div class="case_list_body case_list_body2">
                <ul>
                    <li :class="key%2==0?'yyu':'casela'" v-for="goods,key in goods_list">
                        <a href="">
                            <div class="case_list_body_pic">
                                <img :src="goods.image_url">
                            </div>
                        </a>
                        <div class="case_list_info">
                          <p class="cast_list_tit"><a :href="goods.id">{{goods.title}}</a></p>
                      </div>
                    </li>
                    <div class="clearBoth"></div>
                </ul>
            </div>
        </div>
        <!--资讯列表-->
        <h2 class="floor-title">潮流资讯</h2>
        <div class="newslist">
              <div class="qtao" v-for="news in news_list">
                <div class="mg">
                    <div class="mgl"><img :src="news.image_url" width="100%" /></div>
                    <div class="mgr">
                        <h3>{{news.title}}</h3>
                        <div class="what">
                            <div class="time">
                                <div class="tub"><img src="../image/time.gif" /></div>
                                <div class="shij">{{news.created_time|format}}</div>
                                <div class="clearBoth"></div>
                            </div>
                            <div class="time hit">
                                <div class="tub"><img src="../image/hit.gif" /></div>
                                <div class="shij">{{news.read_count}}</div>
                                <div class="clearBoth"></div>
                            </div>
                            <div class="clearBoth"></div>
                        </div>
                        <div class="jianj">{{news.descript}}</div>
                        <div class="ydu">
                            <div class="anniu"><a href=""><img src="../image/ydu.gif" /></a></div>
                            <div class="clearBoth"></div>
                        </div>
                    </div>
                    <div class="clearBoth"></div>
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
        <div class="bottom-bot">{{site_config.copyright}}</div>
    </div>
  </div>
<script>

  var vm = new Vue({
    el:"#app",
    data:{
      site_config: {},
      nav_list: [],
      banner_list: [],
      goods_list: [],
      news_list: [],
    },
    created(){
      this.get_site_config();
      this.get_nav_list();
      this.get_banner_list();
      this.get_goods_list();
      this.get_news_list();
    },
    filters:{
      format(date_str){
        date_obj = new Date(date_str);
        let year = date_obj.getFullYear();
        let month = date_obj.getMonth()+1;
        let date = date_obj.getDate();
        month = month<10?'0'+month:month;
        date = date<10?'0'+date:date;
        return `${year}-${month}-${date}`;
      }
    },
    methods:{
      jump(link,params){
          api.openWin({
              name: 'page1',
              url: link,
              pageParam: params
          });
      },
      get_site_config(){
        // 获取站点配置
        rpc(settings.API,"Home.site_config",{},result=>{
          this.site_config = result;

          $('#Marquee_x').jcMarquee({ 'marquee':'x','margin_right':'300px','speed':20 });

        });
      },
      get_nav_list(){
        rpc(settings.API,"Home.nav",{},result=>{
          this.nav_list = result;
        });
      },
      get_banner_list(){
        rpc(settings.API,"Home.banner",{},result=>{
          this.banner_list = result;

          // 在获取了数据以后，再进行初始化广告轮播特效
          setTimeout(function(){
            var swiper = new Swiper('.swiper1', {
                pagination : '.pagination1',
                loop: true,
                paginationClickable: true,
                autoplay : 5000,
                grabCursor: true,
                autoHeight: true,
            });
          },1);

        });
      },
      get_goods_list(){
        rpc(settings.API,"Goods.home_goods",{},result=>{
          this.goods_list = result;
        });
      },
      get_news_list(){
        rpc(settings.API,"News.home_news",{},result=>{
          this.news_list = result;
        });
      },
    }
  });

</script>
</body>
</html>
```



### 购物车

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

5. 当在购物车商品列表页中，继续点击"立即付款"，这种类似的按钮时，通过js来获取勾选的商品信息，在服务端生成订单。

6. 对于在蘑菇街中的订单，也是分成2个表，一个事订单信息表，和路飞学城的一模一样，另外有一张订单详情表，这张中把购物车商品的有效期选项去掉，新增一个商品数量。

7. 在生成订单以后，在服务端返回结果以后，调用 APIColud提供的模块微信支付模块完成从蘑菇街跳转到
微信的功能，当然，我们要有对应的微信支付接口才可以完成这个留个，不过，这个流程和支付宝很类似。

```



### flask的第三方模块

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

![1567764568747](F:/%E6%B7%B1%E5%9C%B3python%E5%85%A8%E6%A0%884%E6%9C%9F/12.%E8%98%91%E8%8F%87%E8%A1%97/day07/assets/1567764568747.png)



#### flask-login

flask-login，类似django-auth提供的登录功能

<https://www.jianshu.com/p/01384ee741b6>





## web服务器-Gunicorn

高性能的web服务器软件，经常用于配合flask框架搭建web网站服务。

官网地址：https://gunicorn.org/

安装命令：

```python
pip install gunicorn
pip install gevent
```

在项目的根目录下面终端，可以使用以下命令来启动项目：

```python
gunicorn -w 4 -b 0.0.0.0:5000 manage:app
# gunicorn -w 工作进程 -b 绑定IP:绑定端口 终端脚本文件名:flask实例对象
```

当然我们，一般运行Gunicorn不会一直卡在终端下面运营，肯定以守护进行的方式来运行。

```python
gunicorn -w 4 -b 0.0.0.0:5000 manage:app
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
gunicorn -b 0.0.0.0:5000 -c gunicorn.py manage:app
```


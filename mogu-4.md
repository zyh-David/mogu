# 测试数据

## 添加测试数据

在项目根目录下创建scripts/db_test_data.sql 脚本文件，编写代码如下：

```sql
# 导航菜单
INSERT INTO `moguapp`.`mogu_nav` (`name`, `link`, `parent_id`, `sort`, `is_deleted`, `is_show`, `created_time`, `updated_time`) VALUES
('产品分类', null, null, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('潮流资讯', null, null, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('了解更多', null, null, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('换季新品', null, 1, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('潮流服饰', null, 1, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('时尚搭配', null, 1, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('蘑菇潮流', null, 2, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('风格搭配', null, 2, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),
('品牌资讯', null, 2, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),('关于我们', null, 3, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),('联系我们', null, 3, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21'),('公司地址', null, 3, 0, 0, 1, '2019-06-01 21:33:21', '2019-06-01 21:33:21');

# 轮播广告
INSERT INTO `moguapp`.`mogu_banner` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `title`, `link`, `image_url`) VALUES ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '第一张', '', 'images/banner-1.webp'), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '第二张', '', 'images/banner-2.webp'), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '第三张', '', 'images/banner-3.webp');

# 站点配置
INSERT INTO `moguapp`.`mogu_site_config` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `title`, `name`, `value`, `dtype`) VALUES
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, 'logo图片', 'logo', './images/logo.png', 'image'),
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '版权信息', 'copyright', 'Copyright © 2016 - 2017 Tencent. All Rights Reserved 蘑菇网 ', 'text'),
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '滚动短语', 'phrase', '蘑菇街每天推出时尚服饰、新品搭配、最新潮流及其他时尚前沿资讯等方面的精彩文章，是居家过日子好参谋。欢迎各位美女前来选购！', 'text');

# 文章分类
INSERT INTO `moguapp`.`mogu_news_category` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `name`) VALUES ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '蘑菇潮流'), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '风格搭配'), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '品牌资讯');

# 文章资讯
INSERT INTO `moguapp`.`mogu_news` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `title`, `descript`, `content`, `read_count`, `image_url`, `author`, `is_recommend`, `category_id`) VALUES ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 1, 0, 1, '传统服饰', '晨安、你好、谢谢常挂嘴边，伴跟着邻家女孩的亲和笑脸，发出朴素耐久的魅力。', '清晨，森林里的老鹰和蜗牛都睡醒了，热热烈闹的早会开端了。波点、撞色一个不少，层次丰富，充满童趣的印花似乎化身童话故事里的人物。日子不易，以一颗单纯之心去面临或许会比较简略高兴满意。暂时放下冷静与热心的辩证，化身颜色明澈的精灵，美美地出门吧。

     充分的一天从晨练开端，无惧北风，去慢跑吧，夸姣的身段和永葆年青的状况在勤奋的进程里，让脂肪用力地焚烧吧，留下的是精华和每一天的精彩。

     立体的花瓣均匀散落每一处，淡雅的绿色似乎在向春天招手。它既有毛线衫的优雅温柔，更具卫衣的坚韧耐穿，是非撞色的翻领又是对慎重大气黑色的呼喊，用来做上班打扮也毫不费时，假如温度降了，还能够从衣橱中揪出那件全能的黑色风衣来。', 125, 'images/product/1.jpg', 'admin', 1, 1), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 12, 0, 1, '卫衣', '套头卫衣，有着以一敌百的实用性、包容性和舒适度，信手拈来，搭配短裤短裙打底裤紧身裤等等都各具风情。', '时尚元素总是穿穿梭梭，潮流动态一直来来去去，卫衣则以它最淡然的态度面对瞬息万变的世界。如果你是卫衣粉，定然懂得卫衣的态度；如果你对卫衣不排斥，那么定然会喜欢卫衣的装饰。在许多MM的鞋柜里高跟鞋占据了半壁江山，而且大部分都超过了五公分。也难怪，高跟鞋确实是凸显女人味的利器之一。这样一来，上身的打扮肯定得迎合脚上的高跟，精致的妆容和得体的时装足以让自己在家里倒腾半小时才能出门。终于有一天不用出席正式场合，打开衣柜发现静置已久的卫衣，欣喜地穿上它，忍不住大呼解放了，双脚不用受刑，脸上无需脂粉，如释重负。卫衣上面简简单单的字母或者单词或者图案，无需多加解释，可能代表你的名字，可能是一种调侃，也可能没有什么含义，随性、个性、纯粹、潮流。活跃的字母，耀眼的青春，这就是卫衣的魅力。', 99, 'images/product/2.jpg', 'admin', 1, 1), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 4, 0, 1, '冬装', '冬装，有着以一敌百的实用性、包容性和舒适度，信手拈来，搭配短裤短裙打底裤紧身裤等等都各具风情。它柔软而不柔弱，厚实而不厚重。', '胖妞们经常会在想一个问题，要怎么穿才能显瘦又时尚，或者是穿什么样的服饰才能让自己变得时尚，同样矮个子女生们也是一样烦恼。套头毛衣在寒冷的室外加上抗寒大外套暖暖的不臃肿，温暖的室内脱下防护铠甲也依然是美美的很养眼，这是套头毛衣点石成金的魅力。', 1025, 'images/product/3.jpg', 'admin', 1, 2), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 3, 0, 1, 'Palace x adidas Originals 全新联名鞋款曝光', '作为每个季度的定番，Palace 与 adidas Originals 之间的合作一直十分受人期待。而就在今日，Palace 通过其官方 Instagram 账户释出了一段预告影片，公布了品牌与  adidas Originals 最新的联名企划。', '根据 Palace 所提供的预告影片，双方在本次合作的对象将会是一双采用荧光绿配色的运动鞋。球鞋在鞋舌上搭载有双方 logo 彰显联名属性的同时，还加入了黑色简笔画的小人形象。而 “Das logo mit 3 Palace.” 和 “Never gets old.” 的文字也符合 Palace 一贯以来的幽默搞怪风格。整双球鞋在拥有吸晴配色的同时，细节亦玩味十足。



     据悉，这双全新的联名鞋款将会在本周五登陆 Palace 官网和线下门店，感兴趣的朋友不妨尝试入手。', 2954, 'images/product/4.jpg', 'admin', 1, 2), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 4, 0, 1, 'Quavo 表示自己收藏的球鞋价值高达 300 万美元', '在继 2017 年 Migos 集体登上《Sneaker Shopping》之后，Quavo 于最近又自己再次来到这个节目，在亚特兰大球鞋店 A Ma Maniere 消费了一波。Quavo 在节目中聊到小时候妈妈不让自己买球鞋，在成名之后回馈自己的社区和高中，收到 Finish Line 赠送的终生免费球鞋，同时他还聊到自己收到喜欢的 NBA 球员赠送的比赛穿球鞋，他收藏的球鞋已经价值超过 300 万美元。这次 Quavo 花掉了 11,362.68 美元，对他来说应该也只是 “洒洒水” 吧…', '在继 2017 年 Migos 集体登上《Sneaker Shopping》之后，Quavo 于最近又自己再次来到这个节目，在亚特兰大球鞋店 A Ma Maniere 消费了一波。Quavo 在节目中聊到小时候妈妈不让自己买球鞋，在成名之后回馈自己的社区和高中，收到 Finish Line 赠送的终生免费球鞋，同时他还聊到自己收到喜欢的 NBA 球员赠送的比赛穿球鞋，他收藏的球鞋已经价值超过 300 万美元。这次 Quavo 花掉了 11,362.68 美元，对他来说应该也只是 “洒洒水” 吧…', 388, 'images/product/5.jpg', 'admin', 0, 3), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 7, 0, 1, '回溯英伦历史重塑型格', '2019秋冬See by Chloé受英国乡村传统印花影响，整体呈现浪漫亲和。', '男孩风格与新生女性气质并存，以英式风情爲主题：胡萝卜长裤、浅紫色多孔系带长靴、维多利亚风格褶边衬衫….，其中，针织更是亮点，多以舒适的半羊毛或长羊毛衫形式存在，当然还有Paisley（佩斯里花纹）印花元素与刺绣装饰贯穿始终，无论是俏皮的套装、活泼的连衣裙还是甜蜜的蕾丝上衣，只需搭配一件Paisley单品，就能营造出整体的浪漫氛围。', 325, 'images/product/6.jpg', 'admin', 0, 3), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 4, 0, 1, 'RIMOWA 推出全新材质 iPhone 手机壳', '奢华皮革材质注入。', '在今年年初以品牌标志性的铝镁合金行李箱作为灵感，打造了 iPhone 手机壳之后，顶级旅行箱品牌 RIMOWA 在近期推出了全新材质的 iPhone 手机壳产品。全新的 iPhone 手机壳在保留以往设计的同时，采用了奢华皮革材质取代铝合金，而在内部则继续保留了 TPU 材质来实现防震保护。



     目前该款 iPhone 手机壳已经登陆 RIMOWA 官方网站，售价为 80 欧元，并支持 iPhone XS、iPhone XS Max 两种机型。实用性和高级质感并存的设计，相信一定能给这款手机壳带来十足的人气吧？', 7, 'images/product/14110602.jpg', 'admin', 0, 1), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 9, 0, 1, 'IGOR', 'Tyler, the Creator 公布新专辑《IGOR》巡演信息', 'Tyler, the Creator 将从 8 月 30 日起开启 34 场巡演，第一站将在西雅图打响。接着他将前往芝加哥、纽约、迈阿密、旧金山等城市，并最终于 10 月 26 日在休斯敦完成巡演收官站。此次巡演 Tyler, the Creator 特意邀请了好友 Jaden Smith、GoldLink、Blood Orange 三人作为表演嘉宾随同演出。其中 GoldLink 将全程伴随 Tyler 在北美各大城市的巡演，Jaden Smith 在 9 月期间加入表演，而 Blood Orange 则将出现在 10 月的巡演舞台上。



     演出门票将于美国时间的 6 月 7 日在 GOLF WANG 官方网站进行售卖。



     6/21 – Dover, DE @ Firefly Music Festival
     8/30 – 9/1 – Seattle, WA @ Bumbershoot Festival
     9/2 – Minneapolis, MN @ The Armory*^
     9/4 – Chicago, IL @ Credit Union 1 Arena at UIC*^
     9/6 – Toronto, ONT @ Scotiabank Arena*^
     9/7 – Detroit, MI @ Masonic Temple Theatre*^
     9/10 – Boston, MA @ Agganis Arena*^
     9/11 – Laval, QC @ Place Bell*^
     9/12 – New York, NY @ Madison Square Garden*^
     9/16 – London, UK @ O2 Brixton
     9/17 – London, UK @ O2 Bixton
     9/18 – London, UK @ O2 Brixton
     9/21 – Columbia, MD @ Merriweather Post Pavilion*^
     9/22 – Columbus, OH @ EXPRESS LIVE! Outdoor*^
     9/24 – Pittsburgh, PA @ Stage AE Outdoors*^
     9/25 – Philadelphia, PA @ Skyline Stage at the Mann*^
     9/27 – Orlando, FL @ Addition Financial Arena*^
     9/28 – Tampa, FL @ Yuengling Center*^
     9/29 – Miami, FL @ AmericanAirlines Arena*^
     10/1 – Greensboro, NC @ Greensboro Coliseum Special Events Center*+
     10/3 – Atlanta, GA @ State Farm Arena*+
     10/4 – St. Louis, MO @ Chaifetz Arena*+
     10/5 – Kansas City, MO @ Silverstein Eye Centers Arena*+
     10/7 – Morrison, CO @ Red Rocks Amphitheatre*+
     10/8 – Salt Lake City, UT @ Great Saltair*+
     10/10 – San Francisco, CA @ Bill Graham Civic Auditorium*+
     10/12 – Fresno, CA @ Selland Arena*+
     10/14 – Portland, OR @ Veterans Memorial Coliseum*+
     10/15 – Vancouver, BC @ Pacific Coliseum*+
     10/17 – Reno, NV @ Reno Events Center*+
     10/19 – San Diego, CA @ Pechanga Arena*+
     10/20 – Glendale, AZ @ Gila River Arena*+
     10/22 – Austin, TX @ Frank Erwin Center*+
     10/23 – Dallas, TX @ Theatre at Grand Prairie*+
     10/26 – Houston, TX @ NRG Arena*+

     * = w/ GoldLink
     ^ =w/ Jaden Smith
     + = w/ Blood Orange', 64, 'images/product/14110603.jpg', 'admin', 1, 3), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 5, 0, 1, '致敬经典', 'Supreme x NFL x Raiders x ’47 四方联名系列发布
     以奥克兰突袭者经典 logo 为主要元素。', 'Supreme 在刚刚无预警带来全新联名系列，今次选择向 NFL 联名成立最初球队之一奥克兰突袭者致敬，与美国运动经典 ’47 共同推出一系列服饰和配件。奥克兰突袭者经典 logo 自然是本次联名的重要设计元素，本次将有短袖衬衫、短裤、卫衣、T恤和帽款，辨识度极高的设计无疑是球迷朋友们不能错过的绝佳单品。据悉 Supreme x NFL x Raiders x ’47 四方联名系列将于 6 月 6 日上架纽约、布鲁克林、洛杉矶、伦敦、巴黎门店和线上商城，日本则在稍晚些的 6 月 8 日发售，喜欢的朋友不妨密切留意。', 889, 'images/product/14110604.jpg', 'admin', 0, 3), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', 0, 0, 1, '四川人大排长队也要买的李宁限定', '上周末，李宁接连两天在成都 IFS、锦华路万达店带来 “少不入川” 2019 春夏系列，头顶 30 多度的高温，大批年轻人仍然一早就赶到现场提前排队等候，火爆场面和抢购热情不亚于任何一次话题作品发售。', '近两年，李宁除了惊艳时装周的走秀款式，由 19 秋冬纽约时装周的首席设计师陈李杰主导的 “反伍BADFIVE” 产品线，逐渐进入更多年轻人的视野。“反伍BADFIVE” 发源于街头篮球文化，按照陈李杰本人的解释，BAD 代表叛逆，FIVE 代表篮球里的五个人，表达团队合作的理念。从活塞队坏小子军团汲取灵感，将对抗性的篮球精神注入设计基因。和李宁的运动线和时装周产品有所不同，“反伍BADFIVE” 均是以街头化的视角去诠释服饰，围绕街头篮球这个核心设计，融入嘻哈、涂鸦等 Hip-Hop 元素，态度自由而叛逆，风格实用接地气，更适合日常搭配。除了高辨识度的 Logo 篮球装备，“反伍BADFIVE” 还通过不少联名合作的形式，用街头态度桥接东西方文化。与中国说唱歌手 GAI 合作打造的服饰，T 恤的印花重新诠释了汉字这一传统元素；在美国街头品牌 XLARGE® 合作里，中国风的盘扣夹克则以潮流化剪裁和流行荧光色系得到重塑。而前文提到的 “少不入川” 限定系列，此前由 “反伍BADFIVE” 联手中国街头潮牌 1807 与创意设计单位 WED.CREW 共同打造，向中国巴蜀文化发起致敬，从街头、嘻哈、篮球等多个方面演绎中国风，将 “盖碗茶”“火锅” 等四川特色元素与美式文化的冰球服、卫衣结合在一起，引发众多年轻人抢购，这次 “反伍BADFIVE” 继续带来 “少不入川” 19 春夏系列，同样话题性十足。', 358, 'images/product/14110702.jpg', 'admin', 0, 3);

# 商品分类
INSERT INTO `moguapp`.`mogu_goods_category` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `name`) VALUES ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '换季新品'), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '潮流服饰'), ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '时尚搭配');

# 商品信息
INSERT INTO `moguapp`.`mogu_goods_spu` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `title`, `is_recommend`, `descript`, `effect`, `image_url`, `category_id`) VALUES
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '2016冬季新款韩版长款过膝韩国宽松纯色棉衣', 1, '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', 'images/product/14110707.jpg', 1),
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '2017冬季新款韩版长款过膝韩国宽松纯色棉衣', 1, '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', 'images/product/14110707.jpg', 2),
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '2018冬季新款韩版长款过膝韩国宽松纯色棉衣', 0, '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及,下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', 'images/product/14110707.jpg', 1),
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '2019冬季新款韩版长款过膝韩国宽松纯色棉衣', 1, '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', 'images/product/14110707.jpg', 1),
('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '2019冬季新款韩版长款过膝韩国宽松纯色棉衣', 1, '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', '优质柔软的抓绒棉混纺面料，时尚撞色螺纹圆领，百搭不挑人，长袖， 袖口及下摆撞色螺纹个性拼接，丰富层次感，彰显时尚魅力！胸前爱心，字母图案刺绣点缀，精致美观，很有设计感~宽松的版型，不挑身材哦，内里抓绒，穿着更加的温暖！~推荐', 'images/product/14110707.jpg', 2);
```



## 使用shell脚本来执行测试数据

在scripts目录下创建exec_db_test_data.sh终端shell脚本，代码：

```python
#! /bin/bash
mysql -uroot -p123456 moguapp < ./db_test_data.sql
```

给脚本执行权限

```shell
chmod +x exec_db_test_data.sh
```

直接在scripts目录执行sh脚本

```shell
./exec_db_test_data.sh
```

扩展：

````
我们的python文件也可以像上面的sh脚本一样，可以直接通过设置解析器，给代码文件赋予执行权限来执行一些固定的python代码。例如：

#! /usr/bin/env python3
print("hello")
````





# API接口数据

把各个模块下的api接口全部注册到启动文件中。

manage.py代码：

```python
from apps.modules.common import api
from apps.modules.news import api
from apps.modules.goods import api
```



## 公共模块API接口

公共模块提供站点配置信息，导航菜单，轮播广告等API接口。

common/api.py，代码：

```python
from apps import jsonrpc,jsonrpc2
from .models import Nav, db, Banner,SiteConfig


@jsonrpc.method("Common.nav")
def nav():
    """导航信息"""
    # 查询所有顶级导航数据[parent_id为空的]，并使用sort和id进行
    nav_list = Nav.query.filter(
        Nav.parent_id==None,
        Nav.is_show==True,
        Nav.is_deleted==False
    ).order_by(
        db.desc(Nav.sort),
        db.desc(Nav.id)
    ).limit(5).all()

    data = []
    # 循环每个顶级导航模型，转换成字典
    for nav in nav_list:
        # 顶级导航有可能存在子导航，所以针对子导航也要循环，
        # 并在顶级导航中增加一个字段保存转换字典后的子导航数据
        nav.children_list = []
        top_item = nav.__to_dict__(["id", "name", "link","children_list"])
        for child in nav.children:
            chilren_item = child.__to_dict__(["name","id","link"])
            nav.children_list.append( chilren_item )
        data.append( top_item )

    return data

@jsonrpc.method("Common.banner")
def banner():
    """轮播广告"""
    banner_list = Banner.query.filter(
        Banner.is_show==True,
        Banner.is_deleted==False
    ).order_by(
        db.desc(Banner.sort),
        db.desc(Banner.id)
    ).limit(8).all()

    data = []
    # 循环每个轮播广告模型，转换成字典
    for banner in banner_list:
        item = banner.__to_dict__(["id", "title", "link","image_url"])
        data.append( item )

    return data

@jsonrpc.method("Common.siteconfig")
def siteconfig():
    """站点配置"""
    config_list = SiteConfig.query.filter(
        SiteConfig.is_show==True,
        SiteConfig.is_deleted==False
    ).order_by(
        db.desc(SiteConfig.sort),
        db.desc(SiteConfig.id)
    ).all()
    # 因为站点配置的每一行记录就是一个键值对，所以我们不需要列表保存查询结果，直接一个字典，然后遍历查询结果提取里面的键值对即可
    data = {}

    for item in config_list:
        data[item.name] = item.value

    return data
```



## 文章模块API接口

文章模块提供文章详情，文章列表等数据。

api接口和web开发不一样的地方就在于，我们把提供数据的接口集中一起提供，而不是区分这些数据是否会在同一页页面显示。

news/api.py，代码：

```python
from apps import jsonrpc,jsonrpc2
from .models import db, NewsCategory, News

@jsonrpc.method("News.news_categoty")
def news_category():
    """文章分类"""
    cat_list = NewsCategory.query.filter(
        NewsCategory.is_show==True,
        NewsCategory.is_deleted==False
    ).order_by(
        db.desc(NewsCategory.sort),
        db.desc(NewsCategory.id)
    ).limit(5).all()

    data = []

    for category in cat_list:
        data.append( category.__to_dict__(["id", "name"]) )

    return data

@jsonrpc.method("News.home_news")
def home_news():
    """首页潮流资讯推荐文章"""
    news_list = News.query.filter(
        News.is_recommend==True,
        News.is_show==True,
        News.is_deleted==False
    ).order_by(
        db.desc(News.sort),
        db.desc(News.id)
    ).limit(10).all()
    
    data = []
    for news in news_list:
        data.append( news.__to_dict__(["id", "title", "read_count", "descript", "create_time", "image_url"]) )
    
    return data

@jsonrpc.method("News.listnews(category=Number, page=Number, per_page=Number)")
def listnews(category=0, page=1,per_page=4):
    """列表页文章列表"""
    data = {}
    try:
        query = News.query.filter(
            News.is_show==True,
            News.is_deleted==False
        ).order_by(
            db.desc(News.sort),
            db.desc(News.id)
        )
        
		# 分类查询
        if category > 0:
            query = query.filter(News.category_id==category)

        paginate = query.paginate(page,per_page)
        # 当前分页页码
        data["page"] = paginate.page
        # 当前页数据项
        data["items"] = []
        for item in paginate.items:
            news = item.__to_dict__(["id", "title", "read_count", "descript", "create_time", "image_url"])
            data["items"].append( news )
        # 上一页页码
        data["prev_num"] = paginate.prev_num
        # 下一页页码
        data["next_num"] = paginate.next_num
        # 是否有上一页
        data["has_prev"] = paginate.has_prev
        # 是否有下一页
        data["has_next"] = paginate.has_next
        # 总页码
        data["pages"] = paginate.pages
        # 总数据量
        data["total"] = paginate.total

    except:
        data = []

    return data

@jsonrpc.method("News.news_detail(id=Number)")
def news_detail(id):
    """详情页文章信息"""
    data = {}
    try:
        news = News.query.filter(News.id==id).first()
        data = news.__to_dict__(["id", "title", "author","content","read_count","create_time"])
    except:
        pass

    return data
```



## 商品模块API接口

```python
from apps import jsonrpc,jsonrpc2
from .models import db, GoodsCategory, Goods

@jsonrpc.method("Goods.goods_categoty")
def goods_categoty():
    """商品分类"""
    cat_list = GoodsCategory.query.filter(
        GoodsCategory.is_show==True,
        GoodsCategory.is_deleted==False
    ).order_by(
        db.desc(GoodsCategory.sort),
        db.desc(GoodsCategory.id)
    ).limit(5).all()

    data = []

    for category in cat_list:
        data.append( category.__to_dict__(["id", "name"]) )

    return data


@jsonrpc.method("Goods.home_goods")
def home_goods():
    """首页每日"心"品推荐商品"""
    goods_list = Goods.query.filter(
        Goods.is_recommend == True,
        Goods.is_show == True,
        Goods.is_deleted == False
    ).order_by(
        db.desc(Goods.sort),
        db.desc(Goods.id)
    ).limit(10).all()

    data = []
    for goods in goods_list:
        data.append(goods.__to_dict__(["id", "title", "image_url"]))

    return data



@jsonrpc.method("Goods.list_goods(category=Number, page=Number, per_page=Number)")
def list_goods(category=0, page=1,per_page=5):
    """列表页商品列表"""
    data = {}
    try:
        query = Goods.query.filter(
            Goods.is_show==True,
            Goods.is_deleted==False
        ).order_by(
            db.desc(Goods.sort),
            db.desc(Goods.id)
        )
        
		# 分类ID作为条件查询
        if category > 0:
            query = query.filter(Goods.category_id==category)

        paginate = query.paginate(page,per_page)
        # 当前分页页码
        data["page"] = paginate.page
        # 当前页数据项
        data["items"] = []
        for item in paginate.items:
            goods = item.__to_dict__(["id", "title", "image_url"])
            data["items"].append( goods )
        # 上一页页码
        data["prev_num"] = paginate.prev_num
        # 下一页页码
        data["next_num"] = paginate.next_num
        # 是否有上一页
        data["has_prev"] = paginate.has_prev
        # 是否有下一页
        data["has_next"] = paginate.has_next
        # 总页码
        data["pages"] = paginate.pages
        # 总数据量
        data["total"] = paginate.total

    except:
        data = []

    return data




```



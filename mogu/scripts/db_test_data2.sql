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

# 添加sku库存商品的图片
INSERT INTO `mogu_goods_image` (`created_time`, `updated_time`, `sort`, `is_deleted`, `is_show`, `image_url`, `sku_id`) VALUES ('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 1),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 2),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-3.jpg', 3),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-1.jpg', 4),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 5),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 5),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 6),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 6),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 6),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 7),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8),('2019-06-01 21:33:21', '2019-06-01 21:33:21', null, 0, 1, '../image/product/pro-2.jpg', 8);

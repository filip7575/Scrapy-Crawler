# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class findelItem(scrapy.Item):
    
    link = scrapy.Field()     #链接
    img = scrapy.Field()      #缩略图
    title = scrapy.Field() #商品标题
    code = scrapy.Field()   #商品编号
    price = scrapy.Field()    #商品价格

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class findelItem(scrapy.Item):
    
    link = scrapy.Field()    
    img = scrapy.Field()     
    title = scrapy.Field() 
    code = scrapy.Field()   
    price = scrapy.Field()

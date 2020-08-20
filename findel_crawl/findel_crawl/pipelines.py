# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

from findel_crawl import settings
from findel_crawl.items import findelItem

class DatabasePipeline(object):

   def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()


   def process_item(self, item, spider):
      sql = "INSERT INTO articulos (code, img, link, price, title) VALUES (%s, %s, %s, %s, %s)"
      self.cursor.execute(sql,
                   (
                    item.get("code"),
                    item.get("img"),
                    item.get("link"),
                    item.get("price"),
                    item.get("title")
                   )
                   )
      self.connect.commit()
      return item

   def close_spider(self, spider):
       self.connect.close()

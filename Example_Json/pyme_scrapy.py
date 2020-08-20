from scrapy import Field, Spider, Item, Selector 

class Post(Item):
    url = Field()
    title = Field()

class PythonizameSpider(Spider):
   name, start_urls = 'PythonizameSpider', ['http://pythoniza.me']

   def parse(self, response):
       sel = Selector(response)
       #sites = sel.xpath('//div[@class="col-lg-4 col-md-6 col-sm-6 col-xs-12"]//h3//text()')
       sites = sel.xpath('//div[@class="col-lg-4 col-md-6 col-sm-6 col-xs-12"]')
       items = []

       tex = sites.xpath('//h3//text()').getall()
       lk  = sites.xpath('//a[2]//@href').extract()
       for texto in tex:
          # print(len(tex))
          # p = texto
           post = Post()
           post['title'] = texto
           items.append(post)
       for lin in lk:
           print(lin)
          # p = texto
           post = Post()
           post['url'] = lin
           items.append(post)

       return items



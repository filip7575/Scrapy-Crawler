### Execute

```
scrapy runspider spider.py

2020-08-20 10:03:36 [scrapy.utils.log] INFO: Scrapy 1.8.0 started (bot: scrapybot)
2020-08-20 10:03:36 [scrapy.utils.log] INFO: Versions: lxml 4.4.1.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 19.10.0, Python 2.7.17 (default, Jul 20 2020, 15:37:01) - [GCC 7.5.0], pyOpenSSL 19.0.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Linux-5.3.0-51-generic-x86_64-with-Ubuntu-18.04-bionic
2020-08-20 10:03:36 [scrapy.crawler] INFO: Overridden settings: {'SPIDER_LOADER_WARN_ONLY': True}
2020-08-20 10:03:36 [scrapy.extensions.telnet] INFO: Telnet Password: 086bc4fd7fc98102
2020-08-20 10:03:36 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.corestats.CoreStats']
2020-08-20 10:03:36 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-08-20 10:03:36 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-08-20 10:03:36 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-08-20 10:03:36 [scrapy.core.engine] INFO: Spider opened
2020-08-20 10:03:36 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-08-20 10:03:36 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-08-20 10:03:38 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=> (referer: None)
[<Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>]
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'350.000,00', 'place': u'Centro', 'cod': u'32827'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'803.366,00', 'place': u'Jardim Bot\xe2nico', 'cod': u'32825'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'1.300.000,00', 'place': u'Bosque das Juritis', 'cod': u'32824'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'375.000,00', 'place': u'Centro', 'cod': u'32823'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'450.000,00', 'place': u'Jardim Recreio', 'cod': u'32822'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'1.650.000,00', 'place': u'Jardim Saint Gerard', 'cod': u'32820'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'190.000,00', 'place': u'Jardim Nova Alian\xe7a', 'cod': u'32819'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'250.000,00', 'place': u'Campos El\xedseos', 'cod': u'32818'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'350.000,00', 'place': u'Campos El\xedseos', 'cod': u'32817'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'900.000,00', 'place': u'Ribeir\xe2nia', 'cod': u'32816'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'560.000,00', 'place': u'Jardim Am\xe9rica', 'cod': u'32815'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'750,00', 'place': u'Jardim Interlagos', 'cod': u'32814'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'150.000,00', 'place': u'Cond. Terras de Siena', 'cod': u'32811'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'1.800.000,00', 'place': u'Bonfim Paulista', 'cod': u'32810'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'900.000,00', 'place': u'Cond. Alphaville I', 'cod': u'32809'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:38 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=>
{'price': u'1.790.000,00', 'place': u'Jardim dos Guapor\xe9s', 'cod': u'32808'}
===== END =====
2020-08-20 10:03:38 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2> (referer: None)
[<Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>, <Selector xpath="//div[@class='item col-sm-6 col-md-4 col-lg-3']" data=u'<div class="item col-sm-6 col-md-4 co...'>]
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'250.000,00', 'place': u'Centro', 'cod': u'32807'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'120.000,00', 'place': u'Bonfim Paulista', 'cod': u'32804'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'250.000,00', 'place': u'Alto da Boa Vista', 'cod': u'32803'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'2.000,00', 'place': u'Jardim Nova Alian\xe7a Sul', 'cod': u'32802'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'500.000,00', 'place': u'Jardim Palmares', 'cod': u'32801'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'225.000,00', 'place': u'Alto da Boa Vista', 'cod': u'32800'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'3.000,00', 'place': u'Vila Am\xe9lia', 'cod': u'32798'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'800.000,00', 'place': u'Vila Seixas', 'cod': u'32797'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'260.000,00', 'place': u'Jardim Canad\xe1', 'cod': u'32796'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'Consulte-nos', 'place': u'Jardim Bot\xe2nico', 'cod': u'32795'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'1.490.000,00', 'place': u'Cond. Quinta dos Ventos', 'cod': u'32793'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'850.000,00', 'place': u'Alto da Boa Vista', 'cod': u'32792'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'1.085.000,00', 'place': u'Campos El\xedseos', 'cod': u'32790'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'850.000,00', 'place': u'Jardim Bot\xe2nico', 'cod': u'32789'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'375.000,00', 'place': u'Cond. Evidence Resort', 'cod': u'32788'}
===== END =====
===== BEGIN =====
16
2020-08-20 10:03:39 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2>
{'price': u'1.850.000,00', 'place': u'Jardim S\xe3o Jos\xe9', 'cod': u'32787'}
===== END =====
2020-08-20 10:03:39 [scrapy.core.engine] INFO: Closing spider (finished)
2020-08-20 10:03:39 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 624,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 85265,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 2.398813,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 8, 20, 17, 3, 39, 165586),
 'item_scraped_count': 32,
 'log_count/DEBUG': 34,
 'log_count/INFO': 10,
 'memusage/max': 54632448,
 'memusage/startup': 54632448,
 'response_received_count': 2,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 8, 20, 17, 3, 36, 766773)}
2020-08-20 10:03:39 [scrapy.core.engine] INFO: Spider closed (finished)


```

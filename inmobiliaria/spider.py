import scrapy


class CrawlerSpider(scrapy.Spider):
    name = "zion_crawler"
    start_urls = [
        'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=',
        'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=&&pag=2']

    def parse(self, response):

        count = 0
        items = {}
        page_items = response.xpath("//div[@class='item col-sm-6 col-md-4 col-lg-3']")
        pages_start = response.xpath("//div[@class='pagination']/ul/li/a/@href")[1:8]

        while count < len(page_items):
            print(page_items)
            for zions in response.xpath("//div[@class='item col-sm-6 col-md-4 col-lg-3']"):

                print("===== BEGIN =====")
                print(len(page_items))

                cod = zions.xpath(
                    "//p[@class='corta_desc']/strong/text()").extract()[count]
                price = zions.xpath(
                    "//div[@class='price']/span/text()").extract()[count]
                place = zions.xpath("//h3/small/text()").extract()[count]

                items['cod'] = cod
                items['price'] = price
                items['place'] = place

                yield items
                count+=1
                #print(x)
                print("===== END =====")



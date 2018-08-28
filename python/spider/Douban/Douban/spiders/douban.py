# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douban.items import DoubanItem

class DoubanSpider(CrawlSpider):
    name = 'douban'
    #allowed_domains = ['https://movie.douban.com/top250\?start\=25\&filter\=']
    start_urls = ['https://movie.douban.com/top250?start=']
    page_link = LinkExtractor(restrict_xpaths='//div[@class="paginator"]/a')
    content_link = LinkExtractor(restrict_xpaths='//div[@class="hd"]/a')
    rules = (
#        Rule(page_link,callback="soure",follow=True),
        Rule(content_link,callback="parseitem",follow=False),
    )

    def parseitem(self, response):
        item = ItemLoader(item=DoubanItem(),response=response)
        item.add_xpath("name",'//h1/span/text()')
        item.add_xpath("style",'//span[@property="v:genre"]/text()')
#        item.add_xpath("info",'//span[@property="v:summary"]/text()')
        yield item.load_item() 



    def soure(self,response):
        item = DoubanItem()
        dom = response.xpath("//em/text()").extract()
        for i in dom:
            item["sou"]=i
            yield item

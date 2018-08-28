# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dong.items import DongItem

class DongSpider(CrawlSpider):
    name = 'dong'
#    allowed_domains = ['sun0796.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']
    link_page = LinkExtractor(allow=r"type=4&page=\d+")
    link_content = LinkExtractor(allow='question')
    rules = (
        Rule(link_page, follow=True,callback="page_show"),
        Rule(link_content,callback="page",follow=True)
    )
    def page_show(self,response):
        print(response.url)
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    def page(self,response):
        #print(response.url)
        item = DongItem()
        title = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        item["number"] = title.split('\xa0\xa0')[-2].split(":")[-1]
        item["title"] = title.split('\xa0\xa0')[0].split('：')[1]
        item["content"] = ''.join(response.xpath('//div[@class="c1 text14_2"]/text()').extract())
        yield item
       


# -*- coding: utf-8 -*-
import scrapy
from Picture.items import *
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

    
class PictureSpider(CrawlSpider):
    name = 'picture'
    allowed_domains = ['quanjing.com']
    start_urls = ['http://www.quanjing.com/creative/']
    style = LinkExtractor(restrict_xpaths='//div[@class="indexpic"]/ul/li')
    image_infos = LinkExtractor(restrict_xpaths='//a[@class="item lazy"]')
    rules = (
        Rule(style, callback='style_parse', follow=True),
      #  Rule(image_infos,callback="info_parse",follow=False)
    )
    
    def style_parse(self,response):
        image_urls = response.xpath('//a[@class="item lazy"]/img/@src').extract()
        info_urls = response.xpath('//a[@class="item lazy"]/@href').extract()
        item = PictureItem()
        style = response.xpath('//h1/text()').extract()[0] 
        item["image_path"] = style
        for i in range(len(image_urls)):  
            #在for 循环外面创建item是因为发送请求需要较长时间，在这段时间内item更新，导致发过去的item发生变化
            item = PictureItem()
            item["image_path"] = style
            item["image_url"] = image_urls[i]
            yield scrapy.Request(url="http://www.quanjing.com"+info_urls[i],meta={'item':item},callback=self.info_parse)
    def info_parse(self,response):
       item = response.meta["item"]
       item["title"] = response.xpath('//div[@id="TitleCNDiv"]/div[@class="keylisttitcon"]/text()').extract()[0].strip()
       item["img_type"] = response.xpath('//div[@id="supplier"]/text()').extract()[0].strip()
     #  item["location"] = response.xpath('//div[@id="placeCNDiv"]/ul/li/a/text()').extract()[0].strip()
       yield  item
    def parse_start_url(self, response):
        styles = response.xpath('//div[@class="indexpic"]/ul/li/a/div/text()').extract()
        dir_item =  DirItem()
        for i in styles:
            dir_item["style"] = i
            yield dir_item 

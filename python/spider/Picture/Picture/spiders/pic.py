# -*- coding: utf-8 -*-
import scrapy
from Picture.items import PictureItem,DirItem
import os
class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['quanjing.com']
    start_urls = ['http://quanjing.com//creative/']

    def parse(self, response):
        styles = response.xpath('//div[@class="indexpic"]/ul/li/a/div/text()').extract()
        dir_item =  DirItem()
        for i in styles:
            dir_item["style"] = i
            yield dir_item 
        style_links = response.xpath('//div[@class="indexpic"]/ul/li/a/@href').extract()
        for style_page in style_links:
            style_page = "http://quanjing.com"+style_page
            yield scrapy.Request(style_page,callback=self.style_parse)
    def style_parse(self,response):
        image_urls = response.xpath('//a[@class="item lazy"]/img/@src').extract()
        info_urls = response.xpath('//a[@class="item lazy"]/@href').extract()
        item = PictureItem()
        style = response.xpath('//h1/text()').extract()[0] 
        item["image_path"] = style
        for i in range(len(image_urls)):
            print("---------")
            item["image_url"] = image_urls[i]
            item["i"] = i
            yield scrapy.Request(url="http://www.quanjing.com"+info_urls[i],meta={'item':item},callback=self.info_parse) 

    def info_parse(self,response):
       item = response.meta["item"]
       print(response.request["meta"])
       item["title"] = response.xpath('//div[@id="TitleCNDiv"]/div[@class="keylisttitcon"]/text()').extract()[0].strip()
       item["img_type"] = response.xpath('//div[@id="supplier"]/text()').extract()[0].strip()
       item["location"] = response.xpath('//div[@id="placeCNDiv"]/ul/li/a/text()').extract()[0].strip()
       yield item 

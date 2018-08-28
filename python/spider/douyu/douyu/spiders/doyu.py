# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem
class DoyuSpider(scrapy.Spider):
    name = 'doyu'
    #allowed_domains = ['douyu.com']
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url+str(offset)]

    def parse(self, response):
        data = json.loads(response.text)["data"]
        if len(data)==0:
            return 
        for i in data:
             
            item = DouyuItem()
            item["name"] = i["nickname"]
            item["room_id"] = i["room_id"]
            item["image_urls"] = i["vertical_src"]
            yield item
            self.offset+=20
            yield scrapy.Request(self.url+str(self.offset),callback = self.parse)

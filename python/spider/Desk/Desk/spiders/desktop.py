# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Desk.items import *

class DesktopSpider(CrawlSpider):
    name = 'desktop'
    allowed_domains = ['desktopwallpapers4.me']
    start_urls = ['http://desktopwallpapers4.me/']
    style_links = LinkExtractor(restrict_xpaths='//ul[@class="list1"]/li/a')
    image_links = LinkExtractor(restrict_xpaths='//div[@class="item"]/div[@class="img"]/a')
    page_links = LinkExtractor(restrict_xpaths='//a[@class="item"]')
    pic_link = LinkExtractor(restrict_xpaths='//ul[@class="tags download"]/li/a')
    rules = (
        Rule(style_links, follow=True),
        Rule(page_links,follow=True),
        Rule(image_links,callback="parse_item"),
      #  Rule(pic_link,callback= "parse_item",follow=True)

    )

    def parse_item(self, response):
        img_links = response.xpath('//ul[@class="tags download"]/li/a/@href').extract()
        for url in img_links[:-1]:
            item = DeskItem()
            item["img_url"] = url
            yield item
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

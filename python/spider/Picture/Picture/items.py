# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PictureItem(scrapy.Item):
    # define the fields for your item here like:
    image_path = scrapy.Field()
    image_url = scrapy.Field()
    info_urls = scrapy.Field()
    style = scrapy.Field()
    title = scrapy.Field()
    img_type = scrapy.Field()
    location = scrapy.Field()	
    i = scrapy.Field()
class DirItem(scrapy.Item):
	"""docstring for Dir_item"""
	style = scrapy.Field()
class InfoItem(scrapy.Item):
	title = scrapy.Field()
	img_type = scrapy.Field()
	location = scrapy.Field()	
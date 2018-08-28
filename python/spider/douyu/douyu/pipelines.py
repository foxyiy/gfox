# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class ImagesPipeline(ImagesPipeline):
   def get_media_requests(self, item, info):
       image_url = item['image_urls']
       yield scrapy.Request(image_url)
 def item_completed(self, results, item, info):
 	image_path = [x["path"] for ok, x in results if ok] 
 	img_path = "%s%s"%(self.img_store, item['img_path'])
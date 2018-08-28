# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os,re
from scrapy.pipelines.images import ImagesPipeline

class DeskPipeline(object):
    def process_item(self, item, spider):
        return item

class ImagesPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        yield scrapy.Request(item["img_url"])
    def item_completed(self, results, item, info):
        url = item["img_url"]
        style = url.split("/")[4]
        image_name = re.compile("(\d*).*").findall(url.split("/")[-1])[0]
        pixel = url.split("/")[5]
        path = [x["path"] for ok, x in results if ok]
        dir = "/home/foxyi/Pictures/"+style+"/"+image_name
        if os.path.exists(dir):
            os.rename("/home/foxyi/spider/Desk/Desk/"+path[0],"/home/foxyi/Pictures/"+style+"/"+image_name+"/"+pixel+".jpg")
        else:
            os.makedirs(dir) 
            os.rename("/home/foxyi/spider/Desk/Desk/"+path[0],"/home/foxyi/Pictures/"+style+"/"+image_name+"/"+pixel+".jpg")
            os.rename("/home/foxyi/spider/Desk/Desk/"+path[0],"/home/foxyi/Pictures/"+style+"/"+image_name+"/"+pixel+".jpg")

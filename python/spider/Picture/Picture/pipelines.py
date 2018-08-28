# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import pymongo
from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from Picture.items import *

class PicturePipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname= settings["MONGODB_SHEETNAME"]   
        client = pymongo.MongoClient(host = host, port = port)
        mydb = client[dbname]
        self.sheet = mydb[sheetname]
  
    img_store = get_project_settings().get('IMAGES_STORE')
    def process_item(self, item, spider):
        if isinstance(item,DirItem):
       	    os.makedirs("../images/"+item["style"])
        if isinstance(item,PictureItem):
            self.sheet.insert(dict(item))
        return item
class ImagesPipeline(ImagesPipeline):
    img_store = get_project_settings().get('IMAGES_STORE')
    def get_media_requests(self, item, info):
        if isinstance(item,PictureItem):
            img_url = item["image_url"]
            yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        if isinstance(item,PictureItem):
           path = [x["path"] for ok, x in results if ok]
           os.rename(self.img_store+path[0],"../images"+"/"+item["image_path"]+'/'+path[0][5:])
           return item

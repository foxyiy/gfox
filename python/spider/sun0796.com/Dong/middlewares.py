# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from Dong.settings import USER_AGENTS



class DongDownloaderMiddleware(object):
  
    def process_request(self, request, spider):
       
        user_agent = random.choice(USER_AGENTS)
        print(USER_AGENTS)
        request.headers.setdefault("User_Agent",user_agent)

  

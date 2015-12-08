# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import string
import sys
import os
import shutil
import csv
reload(sys)   
sys.setdefaultencoding('utf8')

class DmozSpider(Spider):
    name = "test"
    allowed_domains = ["mp.weixin.qq.com"]
    start_urls = [
        "http://mp.weixin.qq.com/s?__biz=MzA3OTkxMzMwMQ==&mid=401734464&idx=1&sn=dcb9762f356e3de42012288dee741f42&scene=4",
    ]

    def parse(self, response):
        sel = Selector(response)
        content = sel.xpath('//div[@class="rich_media_content "]//p').extract()
        for i in content:
            print i

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


class Wechat(Spider):
    name = "wechat"
    allowed_domains = ["mp.weixin.qq.com"]
   # linkfile = '/Users/luobu/workspace/python/scrapy/wechat/wechat/conf/nk2015-11-13.csv'
    #start_urls = [
	#"http://mp.weixin.qq.com/s?__biz=MjM5MzAxNjkwMA==&mid=400539304&idx=1&sn=cbb67e8f1bcb8d4926ddb5bbd07d4f8f&scene=4#wechat_redirect"
	#   ]
    
    def __init__(self, category=None, *args, **kwargs):
        linkpath = './wechat/conf/'
        self.donepath = './wechat/conf_done'
        self.articlepath= './wechat/articles/'
        self.start_urls = self.geturls(linkpath)
        
    def geturls(self,linkpath):
        urls = []
        for root,dirs,files in os.walk(linkpath):
            for f in files:
                if os.path.splitext(f)[1]!= '.csv':
                    continue
                linkfile = os.path.join(root,f)
                with open(linkfile,'rb') as csvfile:
                    reader = csv.reader(csvfile)
                    num = 0
                    for line in reader:
                        num = num +1
                        if num <= 2:
                            continue
                        url = line[3]
                        urls.append(url)
                shutil.move(linkfile,os.path.join(self.donepath,f))       
        return urls
        
        
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        #filename = response.url.split("/")[-2] + '.html'
        sel = Selector(response)
        content = sel.xpath('//div[@class="rich_media_content "]//p//text()').extract()
        title = sel.xpath('//title/text()').extract()[0]
        arthur = sel.xpath('//a[@id="post-user"]/text()').extract()[0]
        date = sel.xpath('//em[@id="post-date"]/text()').extract()[0]
        filename = arthur+'_'+date+'_'+title
        filepath = os.path.join(self.articlepath,date,filename)
        if os.path.exists(os.path.join(self.articlepath,date)) == False:
            os.makedirs(os.path.join(self.articlepath,date)) 
        with open(filepath, 'wb') as f:
            f.write(response.url+'\n')
            f.write(''.join(content))
#for i in content:
#	        f.write(i)

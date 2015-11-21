# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import string
import sys
import os
import csv
reload(sys)   
sys.setdefaultencoding('utf8')


class Wechat(Spider):
    name = "wechat"
    allowed_domains = ["mp.weixin.qq.com"]
    linkfile = '/Users/luobu/workspace/python/scrapy/wechat/wechat/conf/nk2015-11-13.csv'
    #start_urls = [
	#"http://mp.weixin.qq.com/s?__biz=MjM5MzAxNjkwMA==&mid=400539304&idx=1&sn=cbb67e8f1bcb8d4926ddb5bbd07d4f8f&scene=4#wechat_redirect"
	#   ]
    
    def __init__(self, category=None, *args, **kwargs):
        linkfile = './wechat/conf/nk2015-11-13.csv'
        self.articlepath= './wechat/articles/'
        self.start_urls = self.geturls(linkfile)
        
    def geturls(self,linkfile):
        
        csvfile = file(linkfile,'rb')
        reader = csv.reader(csvfile)
        urls = []
        num = 0
        for line in reader:
            num = num +1
            if num <= 2:
                continue
            url = line[3]
            urls.append(url)
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
		f.write(''.join(content))
#for i in content:
#	        f.write(i)
        f.close()	

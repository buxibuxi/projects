#提取正文
response.xpath('//div[@class="rich_media_content "]//p//text()').extract()
#提取公号
response.xpath('//a[@id="post-user"]/text()').extract()
#提取title
response.xpath('//title/text()').extract()

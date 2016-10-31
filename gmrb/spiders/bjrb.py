# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gmrb.items import GmrbItem

import datetime

#http://bjrb.bjd.com.cn/html/2016-10/31/node_1.htm
def get_jjrb():
	#先获得时间数组格式的日期
	#starturls=[]
	for i in range(0,365):
		DayAgo = (datetime.datetime.now() - datetime.timedelta(days = i))
		#转换为时间戳:
		#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
		#转换为其他字符串格式:
		otherStyleTime = DayAgo.strftime("%Y-%m/%d")
		yield 'http://bjrb.bjd.com.cn/html/'+otherStyleTime+'/node_1.htm'
	#print(starturls)

class TianjinweSpider(CrawlSpider):
    name = "bjrb"
    allowed_domains = ["bjrb.bjd.com.cn"]
    start_urls = get_jjrb()#['http://paper.ce.cn/jjrb/html/2016-10/28/node_2.htm']


    rules = (
        Rule(SgmlLinkExtractor(allow=r'node_\d{1,2}.htm')),
        Rule(SgmlLinkExtractor(allow=r'content_\d{5}.htm'), callback='parse_item'),
    )


    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//h1/text()').extract_first().strip()
        i['ban']=response.xpath('//div[@class="info"]/span[4]/text()').extract_first().split()[-1]
        #import pdb
        #pdb.set_trace()
        i['date']='-'.join(response.url.split('/')[-3:-1])
        i['content']=u''.join(response.xpath('//div[@class="text"]/descendant::text()').extract())
        return i
# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gmrb.items import GmrbItem

import datetime


def get_jjrb():
	#先获得时间数组格式的日期
	#starturls=[]
	for i in range(0,365):
		DayAgo = (datetime.datetime.now() - datetime.timedelta(days = i))
		#转换为时间戳:
		#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
		#转换为其他字符串格式:
		otherStyleTime = DayAgo.strftime("%Y-%m/%d")
		yield 'http://paper.ce.cn/jjrb/html/'+otherStyleTime+'/node_1.htm'
	#print(starturls)

class TianjinweSpider(CrawlSpider):
    name = "jjrb"
    allowed_domains = ["paper.ce.cn"]
    start_urls = get_jjrb()#['http://paper.ce.cn/jjrb/html/2016-10/28/node_2.htm']


    rules = (
        Rule(SgmlLinkExtractor(allow=r'node_\d{1,2}.htm')),
        Rule(SgmlLinkExtractor(allow=r'content_\d{6}.htm'), callback='parse_item'),
    )


    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//td[@class="font01"]/text()').extract_first()
        i['ban']=response.xpath('//body/table/tr[1]/td[1]/table/tr[1]/td/table[2]/tr/td[2]/text()').extract_first()
        #import pdb
        #pdb.set_trace()
        i['date']='-'.join(response.url.split('/')[-3:-1])
        i['content']=u''.join(response.xpath('//founder-content/descendant::text()').extract())
        return i
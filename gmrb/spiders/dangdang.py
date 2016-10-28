# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from gmrb.items import GmrbItem


class GmwSpider(CrawlSpider):
	name = 'dangdang'
	allowed_domains = ['bang.dangdang.com']
	start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2016-'+str(m)+'-1-'+str(x) for m in range(1,5) for x in range(1,26)]
	rules = (Rule(SgmlLinkExtractor(allow=r'01.00.00.00.00.00-month'),callback='parse_item'),)

	def parse_item(self, response):
		i = GmrbItem()
		url=response.url
		i['name'] = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]').extract()
		i['ban']=''
		i['date']=''
		i['content']=''
		return i

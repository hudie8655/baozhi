# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gmrb.items import GmrbItem

class TianjinweSpider(CrawlSpider):
    name = "tianjinwe"
    allowed_domains = ["epaper.tianjinwe.com"]
    start_urls = ['http://epaper.tianjinwe.com/tjrb/tjrb/2016-10/29/node_1.htm', 'http://epaper.tianjinwe.com/tjrb/tjrb/2016-10/30/node_1.htm', 'http://epaper.tianjinwe.com/tjrb/tjrb/2016-10/31/node_1.htm', ]


    rules = (
         Rule(SgmlLinkExtractor(allow=r'content_\d{7}.htm'), callback='parse_item'),
    )


    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//td[@class="font01"]/text()').extract()[0]
        i['ban']=response.xpath('/html/body/table/tr/td/table/tr/td/table/tr/td/text()').extract()[1]
        i['date']=response.xpath('//span[@class="default"]/strong/text()').extract()[0]
        i['content']=u''.join(response.xpath('//founder-content/descendant::text()').extract())
        return i
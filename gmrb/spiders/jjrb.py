# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gmrb.items import GmrbItem

class TianjinweSpider(CrawlSpider):
    name = "jjrb"
    allowed_domains = ["paper.ce.cn"]
    start_urls = ['http://paper.ce.cn/jjrb/html/2016-10/28/node_2.htm']


    rules = (
        Rule(SgmlLinkExtractor(allow=r'node_\d{1,2}.htm')),
        Rule(SgmlLinkExtractor(allow=r'content_\d{6}.htm'), callback='parse_item'),
    )


    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//td[@class="font01"]/text()').extract()[0]
        i['ban']=response.xpath('/html/body/table/tr/td/table/tr/td/table/tr/td/text()').extract()[1]
        #import pdb
        #pdb.set_trace()
        i['date']='-'.join(response.url.split('/')[-3:-1])
        i['content']=u''.join(response.xpath('//founder-content/descendant::text()').extract())
        return i
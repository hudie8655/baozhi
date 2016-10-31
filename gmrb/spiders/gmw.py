# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from gmrb.items import GmrbItem


class GmwSpider(CrawlSpider):
    name = 'gmw'
    allowed_domains = ['epaper.gmw.cn']
    start_urls = ['http://epaper.gmw.cn/gmrb/html/2016-10/29/nbs.D110000gmrb_01.htm', 'http://epaper.gmw.cn/gmrb/html/2016-10/30/nbs.D110000gmrb_01.htm', 'http://epaper.gmw.cn/gmrb/html/2016-10/31/nbs.D110000gmrb_01.htm',]


    #http://epaper.gmw.cn/gmrb/html/2016-05/07/nbs.D110000gmrb_01.htm
    rules = (
        Rule(SgmlLinkExtractor(allow=r'nbs')),
         Rule(SgmlLinkExtractor(allow=r'nw.*htm$'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//h1/text()').extract()[0]
        i['ban']=response.xpath('//div[@class="lai"]/b/text()').extract()[0].split()[2][:3]
        i['date']=response.xpath('//div[@class="lai"]/b/text()').extract()[0].split()[1]
        i['content']=u''.join(response.xpath('//div[@id="articleContent"]/descendant::text()').extract())
        return i

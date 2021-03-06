# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from gmrb.items import GmrbItem


class QiushiSpider(CrawlSpider):
    name = 'hongqi'
    allowed_domains = ['qstheory.cn']
    start_urls = ['http://www.qstheory.cn/dukan/hqwg/2014/2016-10/20/m_1119756233.htm']#http://m.qstheory.cn/hongqi.htm',]


    #http://www.qstheory.cn/dukan/qs/2016-04/30/m_1118772896.htm
    #http://www.qstheory.cn/dukan/qs/2014/2016-04/15/m_1118596009.htm
    rules = (
        Rule(SgmlLinkExtractor(allow=r'hqwg/2014.*m_\d{10}.htm')),
        Rule(SgmlLinkExtractor(allow=r'hqwg/2016-\d{2}.*m_\d{10}.htm'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//h2/text()').extract()[0]
        i['ban']=response.xpath('//li[@class="l"]/span/text()').extract()[0][10:17]
        i['date']=response.xpath('//li[@class="l"]/text()').extract()[0][2:-2]
        i['content']=u''.join(response.xpath('//div[@class="conBox zoom"]/descendant::text()').extract())
        return i

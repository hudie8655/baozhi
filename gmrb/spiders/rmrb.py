# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from gmrb.items import GmrbItem


class GmwSpider(CrawlSpider):
    name = 'rmrb'
    allowed_domains = ['paper.people.com.cn']
    start_urls = ['http://paper.people.com.cn/rmrb/html/2016-10/02/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-10/01/nbs.D110000renmrb_01.htm',  'http://paper.people.com.cn/rmrb/html/2016-09/17/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/16/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/15/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/14/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/13/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/12/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/11/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/10/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/09/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/08/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/07/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/06/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/05/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/04/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/03/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/02/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-09/01/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/31/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/30/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/29/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/28/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/27/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/26/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/25/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/24/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/23/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/22/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/21/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/20/nbs.D110000renmrb_01.htm',  'http://paper.people.com.cn/rmrb/html/2016-08/17/nbs.D110000renmrb_01.htm', 'http://paper.people.com.cn/rmrb/html/2016-08/12/nbs.D110000renmrb_01.htm', ]




    #http://epaper.gmw.cn/gmrb/html/2016-05/07/nbs.D110000gmrb_01.htm
    rules = (
        Rule(SgmlLinkExtractor(allow=r'nbs')),
         Rule(SgmlLinkExtractor(allow=r'nw.*htm$'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = response.xpath('//h1/text()').extract()[0]
        i['ban']=response.xpath('//div[@class="lai"]/text()').extract()[0].split()[4]
        i['date']=response.xpath('//div[@class="lai"]/text()').extract()[0].split()[3]
        i['content']=u''.join(response.xpath('//div[@id="articleContent"]/descendant::text()').extract())
        return i

# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gmrb.items import GmrbItem

import datetime



class TianjinweSpider(CrawlSpider):
    name = "xxsb"
    allowed_domains = ["dzb.studytimes.cn"]
    start_urls = ['http://dzb.studytimes.cn/index.php?s=%2Findex%2Foldpaper%2Fptype%2Fxxsb%2Fpapername%2F%E5%AD%A6%E4%B9%A0%E6%97%B6%E6%8A%A5&p={}'.format(x) for x in range(1,9)]


    rules = (
        Rule(SgmlLinkExtractor(allow=r'xxsb/\d{8}/$')),
        Rule(SgmlLinkExtractor(allow=r'xxsb/\d{8}/vA\d{1,2}')),
        Rule(SgmlLinkExtractor(allow=r'xxsb/\d{8}/\d{5}.shtml'), callback='parse_item'),
    )


    def parse_item(self, response):
        i = GmrbItem()
        url=response.url
        i['name'] = ' '.join(response.css('div.details h3::text').extract()+ response.css('div.details h4::text').extract())
        i['ban']= response.css('h2.detailsCon_tit i::text').extract_first().split()[-1]
        #import pdb
        #pdb.set_trace()
        i['date']=response.css('h2.detailsCon_tit i::text').extract_first().split()[0]
        i['content']=u'\n'.join(response.css('div#content_div ::text').extract())
        return i
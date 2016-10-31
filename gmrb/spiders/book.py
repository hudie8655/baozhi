# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from gmrb.items import GmrbItem

class BookSpider(CrawlSpider):
    name = "book"
    allowed_domains = ["people.com.cn"]
    start_urls = ['http://theory.people.com.cn/GB/68294/index.html'] + ['http://theory.people.com.cn/GB/68294/index%s.html' %x for x in range(2,9)]
    #start_urls = ['http://theory.people.com.cn/GB/68294/index.html']
    #mport pdb
    #db.set_trace()
    #rules = (
        #Rule(SgmlLinkExtractor(allow=r'\d{6}/index'),callback='parse_index'),
        #Rule(SgmlLinkExtractor(allow=r'\d{4}/\d{4}'), callback='parse_item'),
    #)

    def parse(self,response):
	#self.logger.info(response.css('title::text').extract_first())
	book_index_urls = response.css('div.tw1').xpath('./a[1]/@href').extract()
	for url in book_index_urls:
		yield Request(url,callback=self.parse_index)

    def parse_index(self, response):
	#self.logger.info(response.css('title::text').extract_first())
	#import codecs
	#with codecs.open('bookname.txt','a','gb2312','ignore') as f:
        #    f.write(response.css('title::text').extract_first()+'\n')
	book_name = response.xpath('//h1/text()').extract_first()
	chapter_urls = response.xpath('//div[@class="p1_content"]//a/@href').extract()
	for url in chapter_urls :
		yield Request(url,meta={'book_name':book_name},callback=self.parse_item)

	
    def parse_item(self, response):
	#print(response.url)
	book_name = response.meta['book_name']
	#self.logger.info(response.css('title::text').extract())
	content = ''.join(response.css('div.text_show>p ::text').extract())
	chaptername = response.css('h1::text').extract_first()
	return GmrbItem({'ban':book_name,'name':chaptername,"content":content,'date':''})

# -*- coding: utf-8 -*-
import scrapy

class YlpSpider(scrapy.Spider):
    name = "ylp"
    allowed_domains = ["www.yellowpages.com"]
    start_urls = ['http://www.yellowpages.com/search?search_terms=Translation&geo_location_terms=Virginia+Beach%2C+VA']
    
    
    def parse(self, response):
		companies = response.xpath('//*[@class="info"]')
		
		for company in companies:
			name = company.xpath('h3/a/span[@itemprop="name"]/text()').extract_first()
			phone = company.xpath('div/div[@class="phones phone primary"]/text()').extract_first()
			website = company.xpath('div/div[@class="links"]/a/@href').extract_first()
			yield{'Name':name,'Phone':phone, 'Website':website}
			
			
			
			

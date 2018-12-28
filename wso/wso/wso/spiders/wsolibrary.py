# -*- coding: utf-8 -*-
import scrapy
from wso.items import WsoItem


class WsolibrarySpider(scrapy.Spider):
    name = 'wsolibrary'
    allowed_domains = ['wsolibrary.com']
    start_urls = ['http://wsolibrary.com/']

    def parse(self, response):

         names=response.css('h2.woocommerce-loop-product__title::text').extract()
         URLS=response.css('a.woocommerce-LoopProduct-link.woocommerce-loop-product__link::attr(href)').extract()

         for item in zip(names,URLS):
             newitem=WsoItem()
             newitem['name']=item[0]
             newitem['URL']=item[1]
             yield newitem

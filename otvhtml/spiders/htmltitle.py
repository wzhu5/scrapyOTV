# -*- coding: UTF-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader
from otvhtml.items import Title
# import items

class HtmltitleSpider(scrapy.Spider):
    name = "htmltitle"
    allowed_domains = [l.strip() for l in open('domains.txt').readlines()]
    start_urls = [l.strip() for l in open('urls.txt').readlines()]

    def parse(self, response):
        for sel in response.xpath('//head'):
            item = Title()
            item['request'] = response.url
            item['title'] = sel.xpath('title/text()').extract()
            yield item

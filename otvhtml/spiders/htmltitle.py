# -*- coding: UTF-8 -*-
import scrapy
import csv
import pandas
from scrapy.contrib.loader import ItemLoader
from otvhtml.items import Title
# import items

class HtmltitleSpider(scrapy.Spider):
    name = "htmltitle"

    def __init__(self, file_path='', domain_index='', url_index='', *args, **kwargs):
        super(HtmltitleSpider, self).__init__(*args, **kwargs)
        domain_index_int = int(domain_index)
        url_index_int = int(url_index)
        domains = pandas.read_csv(file_path, usecols=[domain_index_int])
        self.allowed_domains = domains['domain_name'].str.strip('[]').drop_duplicates().values.tolist()
        urls = pandas.read_csv(file_path, usecols=[url_index_int])
        self.start_urls = urls['URL'].str.strip('[]').drop_duplicates().values.tolist()

    def parse(self, response):
        for sel in response.xpath('//head'):
            item = Title()
            item['request'] = response.url
            item['title'] = sel.xpath('title/text()').extract()
            yield item

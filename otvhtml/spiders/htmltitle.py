# -*- coding: UTF-8 -*-
import scrapy
import csv
import pandas
from scrapy.contrib.loader import ItemLoader
from otvhtml.items import Title
# import items

class HtmltitleSpider(scrapy.Spider):
    name = "htmltitle"
    # f = open('OTV_Video_Stream_201609.csv', 'rt')
    cols = pandas.read_csv('OTV_Video_Stream_201609.csv', nrows=0).columns
    domains = pandas.read_csv('OTV_Video_Stream_201609.csv', usecols=[1])
    allowed_domains = domains['domain_name'].str.strip('[]').drop_duplicates().values.tolist()
    print allowed_domains

    print allowed_domains
    # print allowed_domains
    urls = pandas.read_csv('OTV_Video_Stream_201609.csv',    usecols=[7]).values.tolist()
    start_urls = urls.values.tolist()

    def parse(self, response):
        for sel in response.xpath('//head'):
            item = Title()
            item['request'] = response.url
            item['title'] = sel.xpath('title/text()').extract()
            yield item

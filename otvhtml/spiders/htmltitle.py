# -*- coding: utf-8 -*-
import scrapy


class HtmltitleSpider(scrapy.Spider):
    name = "htmltitle"
    allowed_domains = ["v.youku.com"]
    start_urls = ['http://v.youku.com/v_show/id_XMjczMzE1MzI0NA==.html?f=49644767/']

    def parse(self, response):
        filename = 'test'
        with open(filename, 'wb') as f:
            f.write(response.body)

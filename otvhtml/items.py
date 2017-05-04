# -*- coding: UTF-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Title(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    title = scrapy.Field()
    request = scrapy.Field()

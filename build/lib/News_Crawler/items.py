# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class Article(Item):
    url = Field()
    lang = Field()
    title = Field()
    category = Field()
    intro = Field()
    content = Field()
    time = Field()

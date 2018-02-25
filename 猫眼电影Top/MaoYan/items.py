# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影名
    name = scrapy.Field()
    # 发行时间
    release_time = scrapy.Field()
    # 演员
    star = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    pass

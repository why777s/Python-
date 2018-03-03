# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 职位信息的item
class BossItem(scrapy.Item):
    # 职位名称
    name = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 公司名
    company_name = scrapy.Field()
    # 公司信息
    company_info = scrapy.Field()
    # 职位详细介绍
    info_detail = scrapy.Field()

    time = scrapy.Field()

# 职位分类的Item
class TypeItem(scrapy.Item):
    # 职位分类名
    name = scrapy.Field()
    # 链接
    url = scrapy.Field()


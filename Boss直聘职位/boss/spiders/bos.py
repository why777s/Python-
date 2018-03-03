# -*- coding: utf-8 -*-
import scrapy
from boss.items import *
from boss.util import mongo

class BosSpider(scrapy.Spider):
    name = 'bos'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com']

    # 循环生成要爬取的网址
    def start_requests(self):
        mg = mongo.MongoOper()
        pages = []
        # 从mongoDB中获取分类的url
        for i in mg.getTypeUrl():
            url = 'https://www.zhipin.com' + str(i)
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        jobs = response.css('.job-list ul li')
        for job in jobs:
            item = BossItem()
            name = job.css('.info-primary .job-title::text').extract_first()
            salary = job.css('.info-primary .name .red::text').extract_first()
            info_detail = job.css('.info-primary p::text').extract_first()
            company_name = job.css('.info-company .name a::text').extract_first()
            company_info = job.css('.info-company p::text').extract_first()
            time = job.css('.info-publis p::text').extract_first()

            item['name'] = name
            item['salary'] = salary
            item['company_name'] = company_name
            item['company_info'] = company_info
            item['info_detail'] = info_detail
            item['time'] = time
            yield item

        next_page = response.css('.page .next::attr(href)').extract_first()
        if next_page is not None:
            url = 'https://www.zhipin.com' + str(next_page)
            yield scrapy.Request(url=url, callback=self.parse)


# 获取职业分类信息的爬虫，并且将次级网址保存至数据库
class JobTypeSpider(scrapy.Spider):
    name = 'jobType'
    start_urls = ['https://www.zhipin.com']

    def parse(self, response):
        jobTypeMenu = response.css('.job-menu .menu-sub a')
        for jm in jobTypeMenu:
            item = TypeItem()
            name = jm.css('a::text').extract_first()
            url = jm.css('a::attr(href)').extract_first()
            item['name'] = name
            item['url'] = url

            yield item

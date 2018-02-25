# -*- coding: utf-8 -*-
import scrapy
from MaoYan.items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    start_urls = ['http://maoyan.com/board/4']


    def parse(self, response):
        movies = response.css('.main .board-wrapper dd')
        for movie in movies:
            item = MaoyanItem()
            item['name'] = movie.css('.name a::text').extract_first()
            item['release_time'] = movie.css('.releasetime::text').extract_first()
            item['star'] = movie.css('.star::text').extract_first()
            item['score'] = movie.css('.score .integer::text').extract_first() + movie.css('.score .fraction::text').extract_first()
            item['pic'] = movie.css('.board-img::attr(data-src)').extract_first()
            yield item


        next_pages = response.css('.pager-main ul li')
        next_page = next_pages[-1].css('a::attr(href)').extract_first()
        url = response.urljoin(next_page)
        yield scrapy.Request(url=url, callback=self.parse)

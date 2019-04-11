# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/4/9 下午9:07
"""
import scrapy

from ..items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "tb"

    def start_requests(self):
        urls = [
            'https://playsboy.taobao.com/',
            'https://shop136673115.taobao.com/category.htm',
            'https://manfire.taobao.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        cc = response.xpath('//dd[@class="detail"]')
        for item in cc:
            bean = TutorialItem()
            bean['good_name'] = item.xpath('./a/text()').extract()[0]
            bean['url'] = 'https:{}'.format(item.xpath('./a/@href').extract()[0])
            bean['price'] = ''.join(item.xpath('./div/div/span/text()').extract()[1].replace(' ', ''))
            yield bean

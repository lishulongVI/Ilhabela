# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import requests


class TutorialPipeline(object):
    def __init__(self):
        self.file = open('playsboy.json', 'w')

    def process_item(self, item, spider):
        print(dict(item))
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        with open('{}.html'.format(item['good_name'].replace(' ', '')), 'wb') as file:
            file.write(requests.get(item['url']).content)

        print('-----' * 20)
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()

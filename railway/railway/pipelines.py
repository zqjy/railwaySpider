# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv, os, sys
import pandas as pd

from railway.settings import STATION_PATH


class RailwayPipeline(object):
    def open_spider(self, spider):
        if spider.name == 'station_name':
            if not os.path.exists(STATION_PATH):
                with open(STATION_PATH, 'w', encoding='utf-8') as f:
                    csv.writer(f).writerow(('name', 'value'))
            self.reader = pd.read_csv(STATION_PATH)

            self.file = open(STATION_PATH, 'a', encoding='utf-8')
            self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        if spider.name == 'station_name':
            # if self.reader:
            value = item.get('value')
            if value and not value in set(self.reader.value):
                self.writer.writerow([item.get('name'), item.get('value')])
        return item

    def close_spider(self, spider):
        if spider.name == 'station_name':
            # print('-'*5, '数据总数', '-'*5, self.reader.value.count())
            self.file.close()

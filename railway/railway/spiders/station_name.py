# -*- coding: utf-8 -*-
import scrapy, re
from railway.items import StationItem


class StationNameSpider(scrapy.Spider):
    name = "station_name"
    allowed_domains = ["12306.cn"]
    start_urls = ['https://kyfw.12306.cn/otn/resources/js/framework/station_name.js']

    def parse(self, response):
        station_name = response.text
        item = StationItem()
        if len(station_name) > 0:
            station_name = station_name.split('@')

            for name_str in station_name[1:]:
                name = name_str.split('|')
                item['head'] = name[0]
                item['name'] = name[1]
                item['value'] = name[2]
                item['spell'] = name[3]
                item['short_value'] = name[4]
                item['index'] = name[5]
                yield item

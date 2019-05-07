# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RailwayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StationItem(scrapy.Item):
    """
    站点名称
    """
    # @fzh|福州|FZS|fuzhou|fz|29@fzn|福州南|FYS|fuzhounan|fzn|30
    head = scrapy.Field()  # 数据头
    name = scrapy.Field()  # 中文名称
    value = scrapy.Field()  # 实际使用的值
    spell = scrapy.Field()  # 拼音
    short_value = scrapy.Field()  # 简称
    index = scrapy.Field()  # 排序号

class SticketItem(scrapy.Item):
    """
    动车票信息
    """
    train_num = scrapy.Field()  # 车辆编号
    first_seat = scrapy.Field()  # 一等座
    second_seat = scrapy.Field()  # 二等座
    no_seat = scrapy.Field()  # 无座


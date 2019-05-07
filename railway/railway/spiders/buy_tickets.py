# -*- coding: utf-8 -*-
import scrapy


class BuyTicketsSpider(scrapy.Spider):
    name = "buy_tickets"
    allowed_domains = ["12306.cn"]
    start_urls = ['http://12306.cn/']

    def parse(self, response):
        pass

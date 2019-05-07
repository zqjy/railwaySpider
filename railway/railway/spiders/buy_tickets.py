# -*- coding: utf-8 -*-
import scrapy, sys, json
import pandas as pd

from railway.settings import STATION_PATH
from railway.items import SticketItem


class BuyTicketsSpider(scrapy.Spider):
    name = "buy_tickets"
    allowed_domains = ["12306.cn"]
    start_urls = ['http://www.12306.cn/']

    def __init__(self, start='', to='', code='ADULT', date='', *args, **kwargs):
        super(BuyTicketsSpider, self).__init__(*args, **kwargs)
        start_urls = 'https://kyfw.12306.cn/otn/leftTicket/query?' \
                          + 'leftTicketDTO.train_date=%s' \
                          + '&leftTicketDTO.from_station=%s' \
                          + '&leftTicketDTO.to_station=%s' \
                          + '&purpose_codes=%s'
        df = pd.read_csv(STATION_PATH)  # 获取站点数据
        df_dict = dict(zip(list(df.name), list(df.value)))  # 站点数据处理

        # 数据替换
        start = df_dict.get(start)
        to = df_dict.get(to)

        # 生成请求url
        self.start_urls = [start_urls % (date, start, to, code)]

    def parse(self, response):
        train_json = json.loads(response.text)
        ticket_list = []
        if train_json.get('httpstatus') == 200: ticket_list = train_json.get('data').get('result')
        for ticket in ticket_list:
            item = SticketItem()
            info_list = ticket.split('|')
            if info_list[1] != '预订': continue
            item['train_num'] = info_list[3]
            item['first_seat'] = info_list[-13]
            item['second_seat'] = info_list[-9]
            item['no_seat'] = info_list[-8]
            yield item


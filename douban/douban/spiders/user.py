# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class UserSpider(CrawlSpider):
    name = 'user'
    allowed_domains = ['douban.com']
    login_page = 'https://accounts.douban.com/j/mobile/login/basic'
    start_urls = ['https://movie.douban.com/subject/1292052/comments']

    rules = (
        Rule(LinkExtractor(allow=r'\/subject\/.*'), callback='parse_list'),
        # Rule(LinkExtractor(allow=r'\/people\/.*'), callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths='//div[@id="paginator"]//a[@class="next"]'))
    )
    # def __init__(self, pwd):
    #     self.pwd = pwd

    # def start_requests(self):
    #     post_data = {
    #         'ck': '',
    #         'name': '574954033@qq.com',
    #         'password': self.pwd,
    #         'remember': 'false',
    #         'ticket': ''
    #     }
    #     # TODO: 这种返回的类型是啥格式，[]这写法是啥意思
    #     return [FormRequest(self.login_page, formdata=post_data, callback=self.after_login)]

    # def after_login(self, response):
    #     https://movie.douban.com/subject/1292052/commentsfor url in self.start_urls:
    #         yield Request(url, callback=self.user_list)

    def user_list(self, response):
        links = response.xpath(
            '//div[@class="sub_ins"]//div[@class="p12"]/a/@href')
        for link in links:
            yield Request(link, callback=self.parse_item)

    def parse_item(self, response):
        print(response)

    def parse_list(self, response):
        pass
        # items = response.css('.comment-item')
        # for item in items:


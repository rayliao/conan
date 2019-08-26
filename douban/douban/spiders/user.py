# -*- coding: utf-8 -*-
import re
from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from douban.items import UserItem


class UserSpider(CrawlSpider):
    name = 'user'
    allowed_domains = ['douban.com']
    login_page = 'https://accounts.douban.com/j/mobile/login/basic'
    start_urls = ['https://movie.douban.com/subject/1292052/comments']
    rules = (
        Rule(LinkExtractor(allow=r'/people/.*',
                           restrict_xpaths='//div[@class="comment-item"]'), callback='parse_item'),
        # Rule(LinkExtractor(allow=r'\/people\/.*'), callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths='//div[@id="paginator"]//a[@class="next"]'))
    )

    def __init__(self, pwd, *args, **kwargs):
        self.pwd = pwd
        super(UserSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        post_data = {
            'ck': '',
            'name': '574954033@qq.com',
            'password': self.pwd,
            'remember': 'false',
            'ticket': ''
        }
        # TODO: 这种返回的类型是啥格式，[]这写法是啥意思
        return [FormRequest(self.login_page, formdata=post_data, callback=self.after_login)]

    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url)

    def parse_item(self, response):
        # 判断是否请求成功，是否是用户页面
        item = UserItem()
        name = response.xpath(
            '//div[@id="db-usr-profile"]//div[@class="info"]/h1/text()').extract_first()
        item['name'] = str(name).strip()
        url = response.xpath(
            '//div[@id="db-usr-profile"]/div[@class="pic"]/a/@href').extract_first()
        item['url'] = url
        item['account'] = str(url).split('/')[-2]
        item['location'] = response.xpath(
            '//div[@class="user-info"]//a/text()').extract_first()
        revTxt = response.xpath('//p[@class="rev-link"]/a/text()').extract_first()
        item['following'] = int(re.sub(r'\D', '', revTxt))
        yield item

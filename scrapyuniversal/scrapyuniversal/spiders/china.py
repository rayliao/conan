# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose

class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())

class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow=r'article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))    
    )

    def parse_item(self, response):
        loader = ChinaLoader(item = NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_xpath('url', response.url())
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        yield loader.load_item()

from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import PhotoItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/photos/album/1683694782']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }

    rules = (
        Rule(LinkExtractor(allow=r'/album/\d+',
                           restrict_xpaths='//div[@class="photo_wrap"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//link[@rel="next"]'))
    )

    def start_requests(self):
        return [Request('https://accounts.douban.com/j/mobile/login/basic', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        return [FormRequest.from_response(
            response,
            meta={'cookiejar': response.meta(
                'cookiejar')},
            headers=self.headers,
            formdata={
                'ck': '',
                'name': '574954033@qq.com',
                'password': '***',
                'remember': 'false',
                'ticket': ''
            },
            callback=self.after_login,
            dont_filter=True
        )]

    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url, meta={'cookiejar': response.meta['cookiejar']})

    def parse_item(self, response):
        item = PhotoItem()
        item['src'] = response.css('img::attr("src")').extract_first()
        item['content'] = response.css('.pl::text').extract_first()
        yield item

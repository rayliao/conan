import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            # 'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }
        self.login_url = 'https://accounts.douban.com/j/mobile/login/basic'
        self.logined_url = 'https://www.douban.com/photos/album/1683694782'
        self.session = requests.Session()
        self.index = 0

    def login(self, email, pwd):
        post_data = {
            'ck': '',
            'name': email,
            'password': pwd,
            'remember': 'false',
            'ticket': ''
        }
        self.session.post(self.login_url, data=post_data, headers=self.headers)

    def enter(self, url=None):
        if url is None:
            url = self.logined_url
        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            photolst = html.xpath('//div[@class="photo_wrap"]/a/@href')
            self.get_item(photolst)
            nextPage = html.xpath('//link[@rel="next"]/@href')
            if len(nextPage) > 0:
                self.enter(nextPage[0])

    # 获取单张相片信息
    def get_item(self, lst):
        for item in lst:
            response = self.session.get(item, headers=self.headers)
            html = etree.HTML(response.text)
            display = html.xpath(
                '//div[@class="photo_descri"]//span[@id="display"]/text()')
            src = html.xpath('//div[@class="image-show"]//img/@src')
            if len(src) > 0:
                self.save_img(src[0])
            if len(display) > 0:
                with open('./album/title.txt', 'a') as f:
                    f.write(display[0] + '\n')

    # 保存图片
    def save_img(self, src):
        html = requests.get(src)
        with open('./album/' + str(self.index) + '.jpg', 'wb') as f:
            f.write(html.content)
        self.index += 1


if __name__ == '__main__':
    login = Login()
    login.login(email='574954033@qq.com', pwd='wishes--931121')
    login.enter()

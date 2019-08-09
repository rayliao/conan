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

    def enter(self, email, pwd):
        # post_data = {
        #     'ck': '',
        #     'name': email,
        #     'password': pwd,
        #     'remember': 'false',
        #     'ticket': ''
        # }
        response = self.session.post(
            'https://www.douban.com', headers=self.headers)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            result = html.xpath('//div[@class="albums"]//li/a/text()')
            print(result)
        # self.session.post(self.login_url, data=post_data, headers=self.headers)

        # response = self.session.get(self.logined_url, headers=self.headers)
        # html = etree.HTML(response.text)


if __name__ == '__main__':
    login = Login()
    login.enter(email='574954033@qq.com', pwd='wishes--931121')

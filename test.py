import json
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def file():
    with open('./result.txt', 'a') as f:
        f.write('new line')


def demo():
    with open('./result.txt') as f:
        for line in f.readlines():
            l = json.loads(line)
            print(l['title'])


def browser():
    try:
        b = webdriver.Chrome()
        url = 'https://weibo.com/'
        b.get(url)
        wait = WebDriverWait(b, 10)
        wait.until(EC.url_to_be(url))
        name = b.find_element_by_id('loginname')
        pwd = b.find_element_by_name('password')
        name.send_keys('574954033@qq.com')
        pwd.send_keys('931121--wishes')
        submit = b.find_element_by_xpath('//a[@action-type="btn_submit"]')
        submit.click()
        print(submit)
    finally:
        pass


if __name__ == '__main__':
    b = webdriver.Chrome()
    try:
        url = 'https://weibo.com/'
        b.get(url)
        wait = WebDriverWait(b, 10)
        wait.until(EC.url_to_be(url))
        name = b.find_element_by_id('loginname')
        pwd = b.find_element_by_name('password')
        name.send_keys('574954033@qq.com')
        pwd.send_keys('wishes--891002')
        submit = b.find_element_by_xpath('//a[@action-type="btn_submit"]')
        submit.click()
        wait.until(EC.presence_of_element_located((By.ID, 'v6_pl_content_publishertop')))
        input = b.find_element_by_xpath('//textarea[@node-type="textEl"]')
        input.send_keys('publish this message by python using selenium with chromedriver, hooray!')
        btn = b.find_element_by_xpath('//a[@node-type="submit"]')
        btn.click()
        pass
    finally:
        pass

import json
from selenium import webdriver


def file():
    with open('./result.txt', 'a') as f:
        f.write('new line')


def demo():
    with open('./result.txt') as f:
        for line in f.readlines():
            l = json.loads(line)
            print(l['title'])

def browser():
    webdriver.Chrome()


if __name__ == "__main__":
    browser()

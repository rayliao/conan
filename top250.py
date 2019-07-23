import requests
import re
import json
import time


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile(
        '<em class=\"\">(.*?)</em>.*?alt=\"(.*?)\".*?src=\"(.*?)\".*?class=\"inq\">(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'image': item[2],
            'inq': item[3],
        }


def main(offset):
    url = 'https://movie.douban.com/top250?start=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    for i in range(10):
        main(i*25)
        time.sleep(1)

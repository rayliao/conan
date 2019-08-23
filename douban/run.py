import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run():
    pwd = sys.argv[1]
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update({
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    })
    process = CrawlerProcess(settings)
    process.crawl('user', **{'pwd': pwd})
    process.start()


if __name__ == '__main__':
    run()

### Start

```sh
python3 index.py
```

创建项目
```sh
scrapy startproject tutorial
```

创建Spider
```sh
scrapy genspider quotes quotes.toscrape.com
```

运行
```sh
scrapy crawl quotes

scrapy crawl quotes -o quotes.json/quotes.jsonlines

# 其他格式
csv/xml/pickle/marshal/ftp/s3
```
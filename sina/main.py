from scrapy import cmdline

cmdline.execute('scrapy crawl sina1 -a page=30 -a flag=0'.split())

from random import choice
import scrapy


class SunHttpbinIpSpider(scrapy.Spider):
    name = 'sun_httpbin_ip'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']
    proxy_list = [
        "http://14.207.21.136:8080"
    ]
    def start_requests(self):  # 控制爬虫发出的第一个请求
        proxy = choice(self.proxy_list)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)

    def parse(self, response):
        print(response.text)
        pass

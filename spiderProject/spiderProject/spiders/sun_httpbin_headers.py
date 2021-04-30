import scrapy
from scrapy import Request

from fake_useragent import UserAgent

class SunHttpbinHeadersSpider(scrapy.Spider):
    name = 'sun_httpbin_headers'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/headers']

    headers = {
        'User-Agent': UserAgent().chrome
    }
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        print(response.text)
        pass

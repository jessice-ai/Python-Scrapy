
import scrapy
from scrapy import Request
from fake_useragent import UserAgent

class SunHttpbinHeadersSpider(scrapy.Spider):
    name = 'sun_kitchen'
    allowed_domains = ['httpbin.org']
    start_urls = [
        'http://httpbin.org/ip',
        'http://httpbin.org/headers',
        'http://httpbin.org/get',
        'http://httpbin.org/user-agent'
    ]

    headers = {
        'User-Agent': UserAgent().chrome
    }
    def start_requests(self):
        try:
            for url in self.start_urls:
                # print('请求 = %s' % url)
                yield Request(url, headers=self.headers)
        except Exception as result:
            print(result,'false----------------')

    def parse(self, response):
        print(response.text)
        pass

import scrapy
from protego import Protego

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.traceoption.com']
    start_urls = ['http://www.traceoption.com/']

    def start_requests(self):
        cookiesstr=" _ga=GA1.2.1962155546.1608722731; _gid=GA1.2.1809730775.1610007390"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookiesstr.split("; ")}
        yield scrapy.Request(self.start_urls[0],
                            callback=self.parse,
                             cookies=cookies
                                 )
    def parse(self, response):
        quotes = response.css('.el-table__row')
        for quote in quotes:
            option_item=quote.css('.type-image')
            # type=quote.css('.cell')[0]['src']
            # symbol=quote.css('')
            print("测试")
            yield response


            # def parse(self, response):
            #     quotes = response.css('.quote')
            #     for quote in quotes:
            #         text = quote.css('.text::text').extract_first()
            #         author = quote.css('.author::text').extract_first()
            #         tags = quote.css('.tags .tag::text').extract()
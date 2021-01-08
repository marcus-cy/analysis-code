import scrapy
from protego import Protego
from tutorial.items import QuoteItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['www.ihsmarkit.com/info/chi/supplier-highlights.html#sup-high-20-11']
    # start_urls = ['https://ihsmarkit.com/info/chi/supplier-highlights.html#sup-high-20-11']
    # allowed_domains = ['www.traceoption.com']
    # start_urls = ['https://traceoption.com/']
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']


    # def start_requests(self):
    #     cookiesstr=" _ga=GA1.2.1962155546.1608722731; _gid=GA1.2.1809730775.1610007390"
    #     cookies = {i.split("=")[0]: i.split("=")[1] for i in cookiesstr.split("; ")}
    #     print("测试1")
    #     yield scrapy.Request(self.start_urls[0],
    #                         callback=self.parse,
    #                          cookies=cookies
    #                              )
    # def parse(self, response):
    #     # quotes = response.css('.el-table__row')
    #     quotes = response.css('.quote')
    #     # print("response内容 %s" %(response.body))
    #     for quote in quotes:
    #         option_item=quote.css('.type-image')
    #         # type=quote.css('.cell')[0]['src']
    #         # symbol=quote.css('')
    #         print("测试")
    #         yield "测试"
    def parse(self, response):
        quotes = response.css('.quote')
        # print(response.body)
        for quote in quotes:
            item=QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)

import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class LaixuatnganhangSpider(scrapy.Spider):
    name = "laixuatnganhang"
    allowed_domains = ["s.cafef.vn"]
    start_urls = ["https://s.cafef.vn/lai-suat-ngan-hang.chn#data"]

    def __init__(self, *args, **kwargs):
        super(LaixuatnganhangSpider, self).__init__(*args, **kwargs)
        self.driver = None

    def start_requests(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(text=self.driver.page_source)
        for row in sel.xpath('//tbody[@id="tb-interest-rate"]/tr'):
            item = CafefItem()
            item['bank_name'] = row.xpath('.//td[1]/span/text()').get()
            item['no_term'] = row.xpath('.//td[2]/text()').get()
            item['term_1_month'] = row.xpath('.//td[3]/text()').get()
            item['term_3_month'] = row.xpath('.//td[4]/text()').get()
            item['term_6_month'] = row.xpath('.//td[5]/text()').get()
            item['term_9_month'] = row.xpath('.//td[6]/text()').get()
            item['term_12_month'] = row.xpath('.//td[7]/text()').get()
            item['term_18_month'] = row.xpath('.//td[8]/text()').get()
            item['term_24_month'] = row.xpath('.//td[9]/text()').get()
            yield item

    def closed(self, reason):
        if self.driver is not None:
            self.driver.quit()


# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CafefItem(scrapy.Item):
    bank_name = scrapy.Field()
    no_term = scrapy.Field()
    term_1_month = scrapy.Field()
    term_3_month = scrapy.Field()
    term_6_month = scrapy.Field()
    term_9_month = scrapy.Field()
    term_12_month = scrapy.Field()
    term_18_month = scrapy.Field()
    term_24_month = scrapy.Field()
    pass

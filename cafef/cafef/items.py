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

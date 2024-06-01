# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy
from scrapy import Item,Field


class BookscraperItem(scrapy.Item):
    title = Field()
    price = Field()
    upc = Field()
    image_url = Field()
    url = Field()

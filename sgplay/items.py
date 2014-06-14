# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class SgplayItem(Item):
	category = Field()
 	link = Field()
	title = Field()
	desc = Field()
	#autor = Field()
	#rating = Field()

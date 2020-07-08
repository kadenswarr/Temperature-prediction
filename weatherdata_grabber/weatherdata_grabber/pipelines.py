# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class DulpicatesPipeline(object):
	
	def __init__(self):
		self.times_seen = set()
		
	def process_item(self, item, spider):
		if (item['Date'], item['Time']) in self.times_seen:
			raise DropItem("Duplicate time found: %s" % item)
		else:
			self.times_seen.add((item['Date'],item['Time']))
			return item

class TimePipeline(object):

	def process_item(self, item, spider):
		if '53' not in item['Time']:
			raise DropItem("Time does not end in 53")
		else:
			return item 
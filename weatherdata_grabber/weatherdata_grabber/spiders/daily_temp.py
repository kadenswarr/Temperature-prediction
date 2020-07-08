import scrapy
from scrapy_selenium import SeleniumRequest
from datetime import date, timedelta

"""
 This spider is used to scrap yesterday's
 weather from wunderground.com
 
  before running make enable the headless exporter 
 in setting.py
 
 to run spider go to project directory
 and run
 scrapy crawl daily -o filename.csv
 if .csv file exsists it append the new data
"""


class DailySpider(scrapy.Spider):
	name = "daily"
	
	def start_requests(self):
		yesterday = date.today() - timedelta(days=1)
		yesterday = yesterday.strftime("%Y-%m-%d")
		url = "https://www.wunderground.com/history/daily/us/co/denver/KDEN/date/" + yesterday
		yield SeleniumRequest(url=url, callback=self.parse)

	def parse(self, response):
		table = response.css("div.observation-table")
		
		for row in table.css('tr')[1:]:
			yield {
				"Date" : response.url.split("/")[-1],
				"Time" : row.xpath(f'td[1]//text()').get(),
				"Temperature" :  row.xpath(f'td[2]//text()').get(),
				"DewPoint" : row.xpath(f'td[3]//text()').get(),
				"Humidity" : row.xpath(f'td[4]//text()').get(),
				"Wind" : row.xpath(f'td[5]//text()').get(),
				"WinSpeed" : row.xpath(f'td[6]//text()').get(),
				"WindGust" : row.xpath(f'td[7]//text()').get(),
				"Pressure" : row.xpath(f'td[8]//text()').get(),
				"Precip." : row.xpath(f'td[9]//text()').get(),
				"Condition" : row.xpath(f'td[10]//text()').get()
		}
		
		
	
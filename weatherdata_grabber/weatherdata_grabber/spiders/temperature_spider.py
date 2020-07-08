import scrapy
from scrapy_selenium import SeleniumRequest
import csv
from datetime import date, timedelta

"""
 this spider scraps data from wunderground.com
 into a .csv file and is designed for long term
 data 
 
 before running disable the headless exporter 
 in setting.py
 
 to run spider go to project directory in cmd
 and run the command
 scrapy crawl temp -o filename.csv
 if .csv file exsists it append the new data
"""


class TempSpider(scrapy.Spider):
	name = "temp"


	def daterange(self,start_date, end_date): # date range generator
		for n in range(int ((end_date - start_date).days)):
			yield start_date + timedelta(n)

	def start_requests(self):
		base_url = "https://www.wunderground.com/history/daily/us/co/denver/KDEN/date/"
		
		start_date = date.fromisoformat('2020-06-15')
		end_date = date.today() # can be any end date 
		
		# appends dates to the url to get next day
		urls = [base_url + date.strftime("%Y-%m-%d") for date in self.daterange(start_date, end_date)] 
		
		
		for url in urls:
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
		
		
	
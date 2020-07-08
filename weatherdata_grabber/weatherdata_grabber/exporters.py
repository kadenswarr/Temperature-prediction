from scrapy.exporters import CsvItemExporter

"""
made so the csv doesn't get a another header
when appended to exsiting csv files
"""
class HeadlessCsvItemExporter(CsvItemExporter):

	def __init__(self, *args, **kwargs):
		kwargs['include_headers_line'] = False
		super(HeadlessCsvItemExporter, self).__init__(*args, **kwargs)
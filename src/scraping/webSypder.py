import scrapy

from scrapy.http import Request
#import urllib
#urllib.urlretrieve("http://...","file_name.pdf")

#response.css('a::attr(href)').extract() 

class pdfDownloader(scrapy.Spider):
	name = 'pdf_downloader'
	# domain URL
	allowed_domains = ['example.com']
	# links to the specific pages
	url = input('Enter a URL:')
	start_urls = []
	start_urls.append(url)
	print(start_urls)

	def start_requests(self):
		for url in self.start_urls:
			yield Request(url, self.parse)


	def parse(self, response):
		# selector of pdf file.
		selector = 'table tr td a[href$=".pdf"]::attr(href)'
		for href in response.css(selector).extract():
			yield Request(
				url=response.urljoin(href),
				callback=self.save_pdf
			)


	def save_pdf(self, response):
		""" Save pdf files """
		path = response.url.split('/')[-1]
		self.logger.info('Saving PDF %s', path);
		with open(path, 'wb') as file:
			file.write(response.body);


if __name__ == '__main__':
    pdfDownloader = pdfDownloader()
    pdfDownloader.start_requests()
    pdfDownloader.parse()

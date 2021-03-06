import re
import textract
from itertools import chain
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tempfile import NamedTemporaryFile
control_chars = ''.join(map(chr, chain(range(0, 9), range(11, 32), range(127, 160))))
CONTROL_CHAR_RE = re.compile('[%s]' % re.escape(control_chars))
#TEXTRACT_EXTENSIONS = [".pdf", ".doc", ".docx", ""]
TEXTRACT_EXTENSIONS = [".pdf"]
class CustomLinkExtractor(LinkExtractor):
    def __init__(self, *args, **kwargs):
        super(CustomLinkExtractor, self).__init__(*args, **kwargs)
        # Keep the default values in "deny_extensions" *except* for those types we want.
        self.deny_extensions = [ext for ext in self.deny_extensions if ext not in TEXTRACT_EXTENSIONS]
        self.allow = ([r'https://sites.google.com/site/genomicaciencias/lecturas\w+'])
        self.allowed_domains = ['sites.google.com/site/genomicaciencias/lecturas']
#        self.allow = (r'https://sites.google.com/site/genomicaciencias/lecturas'),
#        self.deny = (r'other url patterns to deny'),
class docs_Spider(CrawlSpider):
    name = "docs_Spider"
    start_urls = [
        'https://sites.google.com/site/genomicaciencias/lecturas'
    ]
    rules = (
        Rule(LinkExtractor(
            allow=[r'https://sites.google.com/site/genomicaciencias/lecturas/\w+'],
            restrict_xpaths=(['.//table[@class="filecabinet-table"]/tr[1]',
                              './/table[@class="filecabinet-table"]/tr[2]',
                              './/table[@class="filecabinet-table"]/tr[3]',
                              './/table[@class="filecabinet-table"]/tr[5]',
                              './/table[@class="filecabinet-table"]/tr[6]',
                              './/table[@class="filecabinet-table"]/tr[7]',
                              './/table[@class="filecabinet-table"]/tr[8]',
                              './/table[@class="filecabinet-table"]/tr[9]',
                              './/table[@class="filecabinet-table"]/tr[10]',
                              './/table[@class="filecabinet-table"]/tr[11]',
                              './/table[@class="filecabinet-table"]/tr[12]',
                              './/table[@class="filecabinet-table"]/tr[13]',
                              './/table[@class="filecabinet-table"]/tr[14]',
                              './/table[@class="filecabinet-table"]/tr[15]',
                              './/table[@class="filecabinet-table"]/tr[16]',
                              './/table[@class="filecabinet-table"]/tr[17]',
                              './/table[@class="filecabinet-table"]/tr[18]',
                              './/table[@class="filecabinet-table"]/tr[19]',
                              './/table[@class="filecabinet-table"]/tr[20]',
                              './/table[@class="filecabinet-table"]/tr[21]',
                              './/table[@class="filecabinet-table"]/tr[22]',
                              './/table[@class="filecabinet-table"]/tr[23]',
                              './/table[@class="filecabinet-table"]/tr[24]',
                              './/table[@class="filecabinet-table"]/tr[25]'])


            ),# follow=True

            ),
    #    Rule(LinkExtractor(allow=[r'threads/\w+']), callback='parse_item'),
    )
    # 'https://www.imagescape.com/media/uploads/zinnia/2018/08/20/scrape_me.html'
    # 'https://sites.google.com/site/genomicaciencias/lecturas'
    def __init__(self, *args, **kwargs):
        self.rules = (Rule(CustomLinkExtractor(), follow=True, callback="parse_item"),)
        super(docs_Spider, self).__init__(*args, **kwargs)

    def save_pdf(self, response):
        """ Save pdf files """
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path);
        with open(path, 'wb') as file:
            file.write(response.body);

    def parse_item(self, response):
        self.logger.info('response.url=%s' % response.url)
        if hasattr(response, "text"):
            # The response is text - we assume html. Normally we'd do something
            # with this, but this demo is just about binary content, so...
            pass
        else:
            # We assume the response is binary data
            # One-liner for testing if "response.url" ends with any of TEXTRACT_EXTENSIONS
            extension = list(filter(lambda x: response.url.lower().endswith(x), TEXTRACT_EXTENSIONS))[0]
            if extension:
                self.save_pdf(response)
                # This is a pdf or something else that Textract can process
                # Create a temporary file with the correct extension.
        #        tempfile = NamedTemporaryFile(suffix=extension)
        #        tempfile.write(response.body)
        #        tempfile.flush()
        #        extracted_data = textract.process(tempfile.name)
        #        extracted_data = extracted_data.decode('utf-8')
        #        extracted_data = CONTROL_CHAR_RE.sub('', extracted_data)
        #        tempfile.close()
                with open("scraped_contentReport.txt", "a") as f:
                    f.write(response.url.upper())
                    f.write("\n")
                    #f.write(extracted_data)
                    f.write("\n\n")

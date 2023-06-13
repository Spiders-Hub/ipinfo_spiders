import scrapy


class CountrySpider(scrapy.Spider):
    name = "country"
    start_urls = [
        'https://ipinfo.io/countries/br' #to be replaced by respective country's URL
    ]

    def parse(self, response):
        for row in response.xpath("//table//thead/following::tr"):
            yield {
                'asn':      row.xpath(".//td[1]//text()").get(), #ASN
                'alink':    row.xpath(".//td[1]//@href").get(),  #ASN's link
                'name':     row.xpath(".//td[2]/text()").get(),  #Name
                'numips':   row.xpath(".//td[3]/text()").get(),  #number of IPs 
            }
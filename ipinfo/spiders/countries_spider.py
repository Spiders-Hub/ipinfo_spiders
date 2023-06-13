import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    start_urls = [
        'https://ipinfo.io/countries'
    ]

    def parse(self, response):
        for row in response.xpath("//table//thead/following::tr"):
            yield {
                'country':  row.xpath(".//td[1]//text()").get(), #country
                'clink':    row.xpath(".//td[1]//@href").get(),  #country's link
                'aasns':    row.xpath(".//td[2]/text()").get(),  #allocated ASNs
            }
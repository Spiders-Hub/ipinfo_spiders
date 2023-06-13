import scrapy


class IPRangeDetailSpider(scrapy.Spider):

    name = "ip_range" #spider name 


    #start spider request from here
    def start_requests(self):
        url="https://ipinfo.io/AS749/11.0.0.0/13"
        yield scrapy.Request(url=url, callback=self.parse)


    #spider parser
    def parse(self, response):

        #extract info
        yield {
            "ip_range":response.xpath('//h1[@class="h1-max"]/text()').get(),
            "ip_company":response.xpath('//h2[@class="d-flex align-items-center justify-content-center h5"]/text()').get(),
            "ip_country":response.xpath('//span[@class="flag flag-us"]/text()').get(),
            "domain":response.xpath('//span[@data-content="ASN domain"]/../../td[2]/a/@href').get(),
            "asn":response.xpath('//span[@data-content="ASN this range belongs to"]/../../td[2]/a/@href').get(),
            "registry":response.xpath('//span[@data-content="Name of the registry this address is registered with"]/../../td[2]/text()').get(),
            "number_of_ips":response.xpath('//span[@data-content="Number of IPs hosted on this range"]/../../td[2]/text()').get(),
            "id":response.xpath('//span[@data-content="Identification"]/../../td[2]/text()').get(),
            "whois":response.xpath('//div[@id="block-whois"]//pre/text()').get(),
        }



        
        

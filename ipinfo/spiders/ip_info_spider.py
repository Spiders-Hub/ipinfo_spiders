from pathlib import Path

import scrapy


class IPRangeDetailSpider(scrapy.Spider):

    #spider name
    name = "ip_info"


    #init new equest
    def start_requests(self):
        url="https://ipinfo.io/168.119.85.42"
        
        yield scrapy.Request(url=url, callback=self.parse)


    #parser
    def parse(self, response):

        yield {
            "ip":response.xpath('//h1[@class="h1-max"]/text()').get(),
            "asn_link":response.xpath('//div[@id="block-summary"]//table//tr[1]/td[2]/a/@href').get(),
            "asn_name":response.xpath('//div[@id="block-summary"]//table//tr[1]/td[2]/a/text()').get(),
            "ip_range":response.xpath('//div[@id="block-summary"]//tbody/tr[3]/td[2]/a/text()').get(),
            "ip_range_url":response.xpath('//div[@id="block-summary"]//tbody/tr[3]/td[2]/a/@href').get(),
            "hosted_domains":response.xpath('//div[@id="block-summary"]//tbody/tr[5]/td[2]/text()').get(),
            "privacy":response.xpath('//div[@id="block-summary"]//table//tr[6]/td[2]/text()').get(),
            "anycast":response.xpath('//div[@id="block-summary"]//tbody/tr[7]/td[2]/text()').get(),
            "asn_type":response.xpath('//div[@id="block-summary"]//tbody/tr[8]/td[2]/text()').get(),
            "asn_contact":response.xpath('//div[@id="block-summary"]//table//tr[9]/td[2]/a/text()').get(),
            "city":response.xpath('//div[@id="block-geolocation"]//table//tr[1]/td[2]/text()').get(),
            "state":response.xpath('//div[@id="block-geolocation"]//table//tr[2]/td[2]/text()').get(),
            "country":response.xpath('//div[@id="block-geolocation"]//table//tr[3]/td[2]/a/text()').get(),
            "postal":response.xpath('//div[@id="block-geolocation"]//table//tr[4]/td[2]/text()').get(),
            "local_time":response.xpath('//div[@id="block-geolocation"]//table//tr[5]/td[2]/text()').get(),
            "timezone":response.xpath('//div[@id="block-geolocation"]//table//tr[6]/td[2]/text()').get(),
            "cordinates":response.xpath('//div[@id="block-geolocation"]//table//tr[7]/td[2]/text()').get(),
            "company":response.xpath('//div[@id="block-company"]//strong/text()').get()
        }



        

from pathlib import Path

import scrapy,simplejson


class ASNsSpider(scrapy.Spider):

    name="asn"


    def start_requests(self):
        url="https://ipinfo.io/AS749"
        yield scrapy.Request(url=url,callback=self.parse)
        
        
    def parse(self, response):

        name=response.xpath('//h1[@class="h1-max"]/text()').get().strip()
        full_name=response.xpath('//div[@class="card card-details mt-0"]/h2/text()').get().strip()
        country=response.xpath('//div[@id="block-summary"]//span[contains(@class,"flag")]/text()').get().strip()
        website=response.xpath('//div[@id="block-summary"]//span[@data-content="ASN domain"]/../..//a/@href').get().strip()
        num_hosted_domains=response.xpath('//div[@id="block-summary"]//span[@data-content="Number of domains hosted on this ASN"]/../../td[2]/text()').get().strip()
        number_of_ips=response.xpath('//div[@id="block-summary"]//span[@data-content="Number of IPs hosted on this ASN"]/../../td[2]/text()').get().strip()
        asn_type=response.xpath('//div[@id="block-summary"]//span[@data-content="ISP, business or hosting"]/../../td[2]/text()').get().strip()
        allocated=response.xpath('//div[@id="block-summary"]//span[@data-content="The date this ASN was allocated for use"]/../../td[2]/text()').get().strip()
        updated=response.xpath('//div[@id="block-summary"]//span[@data-content="The date this ASN was last updated"]/../../td[2]/text()').get().strip()
        who_is_pre=response.xpath('//div[@id="block-whois"]//pre/text()').get()

        #get IP ranges info
        ip_ranges_info=[]
        ip_rows=response.xpath('//div[@id="ipv4-data"]/table/tbody/tr')

        for ip_row in ip_rows:
            
            ip_range_url=ip_row.css("a::attr(href)").get()
            ip_range=ip_row.css("a::text").get().strip()
            num_of_ips=ip_row.xpath("//td[3]/text()").get().strip()
            company=ip_row.xpath("//td[2]/span/text()").get().strip()

            ip_ranges_info.append({
                'ip_range':ip_range,
                'url':ip_range_url,
                'num_of_ips':num_of_ips,
                'company':company
            })
            
        yield {
            "name":name,
            "full_name":full_name,
            "country":country,
            "website":website,
            "number_hosted_domains":num_hosted_domains,
            "number_of_ips":number_of_ips,
            "asn_type":asn_type,
            "allocated":allocated,
            "updated":updated,
            "who_is":who_is_pre,
            "ip_ranges":ip_ranges_info
        }
        

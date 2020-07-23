import scrapy
import re
import json

class DressSpider(scrapy.Spider):
    name = 'dress'
    start_urls = ['https://www.lafiancee.com.br/vestidos-de-noiva']

    def parse(self, response):

        for link in response.css('._34sIs').xpath("@href"):
            href = link.get()
            print("Following {}".format(href))
            yield response.follow(href, self.parse)
        
        for script in response.xpath("//script/text()"):
            script = script.get()
            json_search = re.search(r"var warmupData = ({.*});",script,re.DOTALL)
            if json_search != None:
                json_text = json_search.group(1)
                data = json.loads(json_text)
                dress = data["tpaWidgetNativeInitData"]["TPAMultiSection_jenllqhb"]["wixCodeProps"]["product"]

                yield {
                    "id" : dress["id"],
                    "name" : dress["name"],
                    "price" : dress["price"],
                    "media" : [ self.mapMedia(media) for media in dress["media"] ],
                    "options" : [ self.mapOptions(option) for option in dress["options"] ]
                }
    
    
    def mapMedia(self, media):
        return {
            "fullUrl" : media["fullUrl"]
        }

    def mapOptions(self,option):
        return {
            "option" : [ self.mapDomain(domain) for domain in option["selections"] ]
        }
    
    def mapDomain(self,domain):
        return {
            "value" : domain["value"]
        }
    
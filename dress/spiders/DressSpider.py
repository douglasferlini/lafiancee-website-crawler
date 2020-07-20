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
                    "media" : dress["media"],
                    "options" : dress["options"] 
                }
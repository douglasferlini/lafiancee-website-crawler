import scrapy
import re
import json

class LaFianceeSpider(scrapy.Spider):
    name = 'lafiancee_spider'
    start_urls = ['https://www.lafiancee.com.br/vestidos-de-noiva']
    products = []

    def parse(self, response):
        for link in response.css('._34sIs').xpath("@href"):
            href = link.get()
            print("Following {}".format(href))
            yield response.follow(href, self.parse)
        
        #title = ""
        #for title in response.css("._2qrJF").xpath("text()"):
        #    title = title.get()

        for script in response.xpath("//script/text()"):
            script = script.get()
            json_search = re.search(r"var warmupData = ({.*});",script,re.DOTALL)
            if json_search != None:
                json_text = json_search.group(1)
                data = json.loads(json_text)
                dress = data["tpaWidgetNativeInitData"]["TPAMultiSection_jenllqhb"]["wixCodeProps"]["product"]
                yield dress
                #self.products.append(dress)
        
        #yield self.products
        

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
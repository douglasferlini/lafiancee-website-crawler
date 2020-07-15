import scrapy
import re
import json

class LaFianceeSpider(scrapy.Spider):
    name = 'lafiancee_spider'
    start_urls = ['https://www.lafiancee.com.br/vestidos-de-noiva']

    def parse(self, response):
        for link in response.css('._34sIs').xpath("@href"):
            href = link.get()
            print("Following {}".format(href))
            #yield {'page': link.attributes('href').get()}
            yield response.follow(href, self.parse)
        
        title = ""
        for title in response.css("._2qrJF").xpath("text()"):
            title = title.get()
            print(title)

        for script in response.xpath("//script/text()"):
            script = script.get()
            json_search = re.search(r"var warmupData = ({.*});",script,re.DOTALL)
            if json_search != None:
                json_text = json_search.group(1)
                data = json.loads(json_text)
                dress = data["tpaWidgetNativeInitData"]["TPAMultiSection_jenllqhb"]["wixCodeProps"]["product"]
        
                j_product = json.dumps(dress)
                result_file = open("{}.json".format(dress["name"]), "w")
                result_file.write(j_product)
                result_file.close()

        


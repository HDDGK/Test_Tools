import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls=['https://down.ali213.net/pcgame/dredge.html'
              ,'https://haokan.baidu.com/v?pd=wisenatural&vid=17488143471748735348']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response, **kwargs):
        page=response.url_Get.split("/")[-2]
        fileName='quotes-%s.html' % page
        with open(fileName,'wb')as f:
            f.write(response.body)
            self.log('Saved file %s' % fileName)
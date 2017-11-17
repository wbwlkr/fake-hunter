'''
Fake-Hunter stalks possible fakes by searching for copies of a given image url
scrapy runspider hunt.py -o fakes.json
'''

import scrapy

class FakeHunterSpider(scrapy.Spider):
    """Search same pictures accross the web to stalk copies and fakes.
    """
    name = 'fake-hunter'
    start_urls = [
        'https://images.google.com/searchbyimage?'
        'image_url=https://www.cybevasion.fr/chambres/france/35/38666_305220.jpg',
    ]
    custom_settings = {
        'COOKIES_ENABLED': False,
        'DOWNLOAD_DELAY': 2.4,
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'https://images.google.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
        }
    }

    def parse(self, response):
        # parse list of identical images
        for fake in response.css('a[href*="/imgres"]'):
            yield {
                'imgres': fake.css('a::attr("href")').extract_first(),
                'imgurl': 'TODO',
                'imgrefurl': 'TODO',
            }

        # follow pagination link
        next_page = response.css('#nav td.cur + td a.fl::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

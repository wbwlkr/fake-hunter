'''
Sauceplz stalks possible fakes by searching for source and copies of a given image url
scrapy runspider sauceplz.py -o fakes.json
'''

from urllib.parse import urlsplit, parse_qs
import scrapy

class SaucePlzSpider(scrapy.Spider):
    """Search same pictures accross the web to stalk copies and fakes.
    """
    name = 'sauce-plz'
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
            urltosplit = fake.css('a::attr("href")').extract_first()
            params = parse_qs(urlsplit(urltosplit).query)
            yield {
                'domain': urlsplit(params['imgrefurl'][0]).netloc,
                'image': params['imgurl'][0],
                'sauce': params['imgrefurl'][0],
            }

        # follow pagination link
        next_page = response.css('#nav td.cur + td a.fl::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

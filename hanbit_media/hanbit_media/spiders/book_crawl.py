# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    # 크롤러의 이름 실제 크롤링할 때 사용함.
    name = 'book_crawl'
    
    # 크롤러 실행을 허용할 도메인을 지정.
    # 해당 서버에서 실행되다가 허용된 도메인 이외는 무시합니다.  
    allowed_domains = ['hanbit.co.kr']
    #리스트로 지정해 한번에 여러 웹 페이지에서 크롤링을 시작하게 할 수 있습니다.
    start_urls = [
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=001',
        'http://www.hanbit.co.kr/store/books/category_list.html?cate_cd=002',
    ]

    rules = (
        Rule(LinkExtractor(allow=r'store/books/look.php\?p_code=.*'),
         callback='parse_item', follow=True),

        Rule(LinkExtractor(allow=
            r'store/books/category_list\.html\?page=\d+&cate_cd=00\d+&srt=p_pub_date'))
        # callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        # 책이름
        
        i['book_title'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract()

        # 저자 이름
        i['book_author'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="저자 : "]/span/text()').extract()

        # 번역자 이름
        i['book_translator'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="번역 : "]/span/text()').extract()

        # 출간일 
        i['book_pub_date'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="출간 : "]/span/text()').extract()


        # SIBN
        i['book_isbn'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="ISBN : "]/span/text()').extract()

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

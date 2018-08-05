
1.
pipenv install Twisted python version 
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

2.
pipenv install scrapy

3.
scrapy startproject hanbit_media

4.
items.py 수정
    크롤링할 목록 이름 등등
5.
스파이더 만들기
scrapy genspider -t crawl book_crawl hanbit.co.kr
    # spiders 경로에 생성

6.
생성된 book_crawl 파일 수정

7.
크롤링 실행
    scrapy crawl <크롤링 이름> -o <출력파일 이름> -t <출력 형식>
scrapy crawl book_crawl -o book_list.csv -t csv



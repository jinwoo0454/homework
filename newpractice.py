import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://m.blog.naver.com/kiddwannabe/221177292446')
soup = BeautifulSoup(data.text, 'html.parser')

client = MongoClient('localhost', 27017)
db = client.dbsparta

# select를 이용해서, tr들을 불러오기
blog_title = soup.select_one('.Nicon_service')
print(blog_title.text)

# movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         print(a_tag.text)




tr_list = soup.select('#old_content > table > tbody > tr')

for tr in tr_list:
    name =  tr.select_one('.tit5 > a')
    rank = tr.select_one('td.point')
    if name is not None:
        print(name.text)
    if rank is not None:
        print(rank.text)

        # old_content > table > tbody > tr:nth-child(2) > td.point
#old_content > table > tbody > tr:nth-child(2) > td.title > div
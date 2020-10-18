import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

client = MongoClient('localhost', 27017)
db = client.genie

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


for tr in trs:
    rank = tr.select_one('td.number')
    title = tr.select_one('td.info > a.title')
    artist = tr.select_one('td.info > a.artist')
    print(rank.text[:2].strip(),title.text.strip(),artist.text)
    genie ={
        'rank': rank.text[:2].strip(),
        'title': title.text.strip(),
        'artist': artist.text
    }
    db.genie.insert_one(genie)



#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

#url_list에 있는 사이트에 가서 title, image, category, url 각각 db에 저장하기
url list =
https://www.tkbell.co.kr/user/main.do?sso=ok
https://zoom.us/
https://ko.padlet.com/
https://www.tkbell.co.kr/user/main.do?sso=ok
https://www.mentimeter.com/
https://kahoot.com/
https://www.mangoboard.net/index.do
https://www.flaticon.com/
https://www.quizn.show/
https://www.speakpipe.com/
https://obsproject.com/ko
https://www.liveworksheets.com/
https://www.onthe.live/
https://quickdraw.withgoogle.com/
https://www.e2esoft.com/ivcam/
https://www.tkbell.co.kr/user/main.do?sso=ok
https://info.flipgrid.com/
https://class123.ac/
https://pixelmob.co/
https://tinypng.com/
https://www.onelink.to/
https://beecanvas.com/business


# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get(url, headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
category = soup.select_one('meta[property="og:description"]')['content']
url = soup.select_one('meta[property="og:url"]')['content']
print(title, category, image, url)

doc = {
    'id': 30000 ~ 30022,
    'title': title,
    'category': category,
    'image': image,
    'url': url
}
db.tools.insert_one(doc)

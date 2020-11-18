from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

driver = webdriver.Chrome('chromedriver')
page = 20000  # position of current page

while page < 30000:
    page = page + 1
    base_url = "https://edtechkorea.or.kr/fairOnline.do?EX_IDX=417&selAction=detail&hl=KOR&ITEM_IDX="
    driver.get(base_url + str(page))
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    #prodTitle
    prodTitle = soup.select_one('.prodTitle')
    if prodTitle is None:
        continue
    #도구 이름
    title = prodTitle.text
    #도구 카테고리
    category = ''
    categorys = soup.select('.prodInfo > ul > li > p > span')
    for item in categorys:
        category += item.text+' '

    #이미지url
    img_url_src = soup.select_one('ul.slider-for.slick-initialized.slick-slider > div > div > li > span > img')
    if img_url_src is None:
        continue
    img_url_src = img_url_src['src']
    img_base_url = 'https://edtechkorea.or.kr'
    img_url = img_base_url + img_url_src

    #도구 사이트 url
    url = soup.select_one('#con_container > div > section.compArea > table > tbody > tr:nth-child(2) > td:nth-child(4)').text

    doc = {
        'id': page,
        'title': title,
        'category': category,
        'image': img_url,
        'url': url
    }
    db.tools.insert_one(doc)
    print(title, category,img_url, url)
driver.quit()  # 끝나면 닫아주기
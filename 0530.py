import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://news.naver.com/breakingnews/section/101/259"
header ={'user-agent':'Mozilla/5.0'}
res = requests.get(url,headers=header)
soup = BeautifulSoup(res.text,'lxml')

# print(soup)
#뉴스 제목과 링크 주소 가져오기
new_list=[]
tag3=soup.find('ul',{'class':'sa_list'}).find_all('li',limit=3)
for li in tag3:
    new_info={"title":li.find('strong', {'class':'sa_text_strong'}).text,
              "news_url":li.find('a')['href']
              }
    new_list.append(new_info)

for new in new_list:
    de_url = new['news_url']
    de_res = requests.get(de_url,headers=header)
    de_soup = BeautifulSoup(de_res.text,'lxml')
    print(de_url)

    body = de_soup.find('article',{'class':'go_trans _article_content'})
    new_content = body.text.replace('\n',' ').strip()
    new['news_contents'] = new_content

df = pd.DataFrame(new_list)

print(df)



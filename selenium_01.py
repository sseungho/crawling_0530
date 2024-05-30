from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd

url = "https://www.naver.com/"

# 브라우져 꺼짐 방지
opt = Options()
opt.add_experimental_option('detach', True)
# opt.add_argument('headless')

driver = webdriver.Chrome(options=opt)
driver.get(url)
# time.sleep(2)

# 검색창에 키워드 입력 + 엔터
searchBox =  driver.find_element(By.ID, 'query')
searchBox.send_keys('인공지능')
searchBox.send_keys(Keys.RETURN)

# 뉴스탭 클릭
# driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[2]/div[2]/a/span/i').click()
# time.sleep(0.1)
driver.find_element(By.LINK_TEXT,'뉴스').click()

# 화면 스크롤
scroll = driver.find_element(By.TAG_NAME, 'body')
for i in range(30):
    scroll.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

# 누스 제목 추출
newsTitle = driver.find_elements(By.CLASS_NAME,'news_tit')
# print(newsTitle[0].text)
count=1
newsList = []
for i in newsTitle:
    # print(count, "," +  i.text)
    with open("news.csv",'w', encoding='utf-8') as f:
        f.write(str(count) + "," + i.text)
        f.write('\n')
    newsList.append(i.text)
    count+=1

data = pd.DataFrame(newsList)
print(data)
driver.quit()





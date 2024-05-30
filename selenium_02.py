from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd

singer = input("가수 입력: ")


url = "https://www.melon.com/index.htm"

# 브라우져 꺼짐 방지
opt = Options()
opt.add_experimental_option('detach', True)
# opt.add_argument('headless')

driver = webdriver.Chrome(options=opt)
driver.get(url)
# time.sleep(2)

# 검색창에 키워드 입력 + 엔터
searchBox =  driver.find_element(By.ID, 'top_search')
searchBox.send_keys(singer)
searchBox.send_keys(Keys.RETURN)
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="divCollection"]/ul/li[4]/a').click()
time.sleep(1)


driver.find_element(By.XPATH,'//*[@id="frm"]/div/ul/li[13]/div/a[1]').click()

time.sleep(1)
titleList = []
lyricList = []
for i in range(1, 12):
    try:
        xpTitle = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/div/div[1]/span/a'
        title = driver.find_element(By.XPATH, xpTitle).text
        titleList.append(title)

        xpLyric = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[3]/div/a'
        driver.find_element(By.XPATH, xpLyric).click()
        lyric = driver.find_element(By.ID, 'd_video_summary').text.replace('\n', ' ')
        lyricList.append(lyric)
        driver.back()
        time.sleep(1)

    except:
        pass

data = pd.DataFrame()
data['노래 제목'] = titleList
data['노래 가사'] = lyricList
data.to_excel(f'{singer}.xlsx', engine='openpyxl')

driver.quit()


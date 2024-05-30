from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request

import time
import pandas as pd
import os

keyword = input("검색어 입력: ")
search = f"{keyword} 무료 png"


url = "https://www.google.co.kr/"

# 이미지 저장 폴더 생성
save_dir = 'images_google'
os.makedirs(save_dir, exist_ok=True)

# 브라우져 꺼짐 방지
opt = Options()
opt.add_experimental_option('detach', True)
# opt.add_argument('headless')

driver = webdriver.Chrome(options=opt)
driver.get(url)
# time.sleep(2)

# 검색창에 키워드 입력 + 엔터
searchBox = driver.find_element(By.ID, 'APjFqb')
searchBox.send_keys(search)
searchBox.submit()
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()

links = []
images = driver.find_elements(By.CSS_SELECTOR,'g-img.mNsIhb>img.YQ4gaf')
# print(images[0].get_attribute('src'))
print(len(images))
for img in images:
    if img.get_attribute('src') != None:
        links.append(img.get_attribute('src'))


# 이미지 저장
for i,u in enumerate(links):
    urllib.request.urlretrieve(u, './'+save_dir+'/cat_'+str(i)+'.jpg')
    time.sleep(0.2)
print('END')
driver.quit()



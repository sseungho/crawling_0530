import requests
import json

# 다음 검색
url = "https://dapi.kakao.com/v2/search/web"

restApiKey = "5772b0933388bad3ba4e140905605519"
myHeader = {'Authorization': 'KakaoAK ' + restApiKey}
reqParams = {'query':'인공지능',
           'page': 1,
           'sort': 'accuracy'}

response = requests.get(url,params=reqParams, headers=myHeader)

# print(response.status_code)
result = response.json()
print(len(result['documents']))

for i in range(1, 11):
    print(result['documents'][i]['contents'])




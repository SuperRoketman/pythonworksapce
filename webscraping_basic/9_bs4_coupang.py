# HTML GET방식 : ?, & 사용 (?와 & 뒤에 변수와 값을 넣음)
#   값들을 원하는 값으로 변경하여 쉽게 페이지 요청 가능
#   한번 전송할 때 보낼 수 있는 양이 제한적이어서 큰 데이터는 전송 X
#   보안 데이터를 전송하기엔 알맞지 않음. POST도 그리 안전하진 않지만 GET보단 안전

# HTML POST방식 : ?? 안 알려주네

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
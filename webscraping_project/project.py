import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(idx, title, link):
    print("{}. {}".format(idx+1, title))
    print("  (링크 : {})".format(link))



def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9B%90%EC%A3%BC+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 어제보다 oo도 낮아요, 날씨
    cast = soup.find("p", attrs={"class":"summary"}).get_text().replace("  ", " / ")
    # 현쟈 oo도 (최저 최고 기온)
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace(" 현재 온도", "현재 온도 :")
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온", "최저기온 : ") # 최저 기온
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("최고기온", "최고기온 : ")

    rainfall1 = soup.find_all("span", attrs={"class":"weather_inner"})[0]
    rainfall2 = soup.find_all("span", attrs={"class":"weather_inner"})[1]
    rainfall_am = rainfall1.find("span", attrs={"class":"weather_left"}).get_text().replace(" 오전 ", "오전 : ")
    rainfall_pm = rainfall2.find("span", attrs={"class":"weather_left"}).get_text().replace(" 오후 ", "오후 : ")


    dust1 = soup.find_all("li", attrs={"class":"item_today level1"})[0]
    dust2 = soup.find_all("li", attrs={"class":"item_today level1"})[1]
    pm10 = dust1.find("a").get_text().replace(" 미세먼지 ", "미세먼지 : ")
    pm25 = dust2.find("a").get_text().replace(" 초미세먼지 ", "초미세먼지 : ")

    #  출력
    print(cast)
    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("강수확률 ({}/ {}\b)".format(rainfall_am, rainfall_pm))
    print("{}".format(pm10))
    print("{}".format(pm25))
    print()
    print("="*60)
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(idx, title, link)
    print()
    print("="*60)
    print()


def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1

        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find_all("a")[a_idx]["href"]
        print_news(idx, title, link)


if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
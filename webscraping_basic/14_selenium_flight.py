from selenium import webdriver
browser = webdriver.Chrome()

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

# 가는날 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 이번 달 27, 28일 선택
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button').click()

# 네이버 항공권 웹이 바뀌어 뭐가 안됨.
# Quiz) Selenium 을 이용하여 아래 업무를 자동으로 수행하는 프로그램을 작성하시오
# 1. https://www.w3school.com 접속 (URL 은 구글에서 w3schools 검색)
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
#  First Name : 나도
#  Last Name : 코딩
#  Country : Canada
#  Subject : 퀴즈 완료하였습니다.
#  * 위 값들은 변수로 미리 저장할 것
# 6. 5초 대기 후 Submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/')
browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[112]').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contect")]').click()

fname = browser.find_element_by_xpath('//*[@id="fname"]')
fname.send_keys('나도')
lname = browser.find_element_by_xpath('//*[@id="lname"]')
lname.send_keys('코딩')
country = browser.find_element_by_xpath('//*[@id="country"]/option[2]')
country.click()
subject = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
subject.send_keys('퀴즈 완료하였습니다.')

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()
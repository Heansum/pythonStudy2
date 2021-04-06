from selenium import webdriver
import APP
from selenium.webdriver import ActionChains
import time

driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz.Knqxbd.tzLNed > ul > li.uQeS5e.qKjvAb.iZhiic > a > span > span.pvVVcb")
element.click()

element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz:nth-child(3) > c-wiz > div > div > div > div:nth-child(4) > div > a")
element.click()

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.Z3lOXb > div.xwY9Zc > a")
element.click()

''' 페이지에 들어가자마자 50위까지의 순위 수집 '''
# 순위를 수집하는 코드
elementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div")
# 수집한 순위의 마지막 요소
lastElement = elementList[-1]
# 마지막 요소로 스크롤을 이동시켜라
ActionChains(driver).move_to_element(lastElement).perform()
''' 페이지에 들어가자마자 50위까지의 순위 수집 '''

# 스크롤을 내리고 3초 쉬도록
# 스크롤을 내리자마자 바로 새롭게 불러온 순위를 수집하면
# 새롭게 불러오기전에 아래 코드가 실행되므로
# 정상적으로 동작하지 않음
# 그래서 스크롤을 내리고 추가로 순위 데이터를 불러올 수 있도록 3초정도 여유 시간을 주는 것

''' 스크롤을 내려서 새롭게 불러온 순위 수집 '''
for i in range(1, 4) :
    time.sleep(3)

    # 순위를 수집하는 코드
    elementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz")
    # 수집한 순위의 마지막 요소
    lastElement = elementList[-1]
    # 마지막 요소로 스크롤을 이동시켜라
    ActionChains(driver).move_to_element(lastElement).perform()

appInfoList = []

# 앱의 데이터를 뽑아서 객체에 저장
for element in elementList:
    appName = element.find_element_by_css_selector(".WsMG1c.nnK0zc")
    appName = appName.text

    company = element.find_element_by_css_selector(".KoLSrc")
    company = company.text

    appInfo = APP.APPInfo(appName, company)
    appInfoList.append(appInfo)

print("가져온 앱의 개수 = ", len(appInfoList))

for appInfo in appInfoList:
    print("%s / %s" % (appInfo.getAppName(), appInfo.getCompany()))
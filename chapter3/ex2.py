from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

element = driver.find_element_by_css_selector('#gbqfq')
element.send_keys("네이버")

element.send_keys(Keys.ENTER)

time.sleep(1)


# element = driver.find_element_by_css_selector('#gbqfb > span')
# element.submit()

time.sleep(1)

element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)

# 검색어 영역에 코리아교육그룹 이라고 입력하고
# element = driver.find_element_by_css_selector('#gbqfq')

time.sleep(1)

# 검색 영역에 기존에 입력했던 내용 삭제
# element.clear()
element.send_keys("코리아교육그룹")


# 해당 앱을 검색하고자 함
time.sleep(1)

element.send_keys(Keys.ENTER)
# element = driver.find_element_by_css_selector('#gbqfb > span')
# element.submit()

time.sleep(1)

element = element.find_element_by_css_selector('#gbq1 > div > a > img')
element.submit()

# print(element.get_attribute("href"))
# print(element.get_property("class"))
#
# print(element.is_displayed())
# print(element.is_enabled())
# print(element.is_selected())
#
# print(element.value_of_css_property("position"))
#
# print(element.screenshot("element.png"))

# print("id = ", element.id)
# print("tag_name = ", element.tag_name)
# print("location = ", element.location)
# print("location_once_scrolled_into_view = ", element.location_once_scrolled_into_view)
# print("size = ",element.size)
# print("rect= ", element.rect)
# print("text = ", element.text)
# print("parent = ", element.parent)













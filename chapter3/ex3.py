from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a")
ActionChains(driver).move_to_element(element).perform()

time.sleep(1)

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a")
ActionChains(driver).move_to_element(element).perform()

time.sleep(1)

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(3) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a")
ActionChains(driver).move_to_element(element).perform()

time.sleep(1)









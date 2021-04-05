from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a

elementList = driver.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div')
for element in elementList:
    elementName = element.find_element_by_css_selector(".WsMG1c.nnK0zc")
    elementName = elementName.text
    print(elementName, "페이지에 접속")
#.WHE7ib.mpg5gc
    element.click()

    time.sleep(1)

    driver.back()





from selenium import webdriver

driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://www.naver.com"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)







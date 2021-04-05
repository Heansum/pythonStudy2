from selenium import webdriver
import time


driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)

# 셀레니움의 기본 대기 시간은 0초
# 셀레니움의 기본 대기 시간을 10초로 설정
driver.implicitly_wait(10)







# elementList = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div:")
# for element in elementList:
#     print(element)


# elementList2 = driver.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div')
# for element in elementList2:
#     print(element)
#
# elementList = driver.find_elements_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]')
# for element in elementList:
#     print(element)






element = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[1]/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a')

element.click()

time.sleep(2)

print("현재 페이지에서 뒤로가기")
driver.back()
time.sleep(2)

print("현재 페이지에서 앞으로가기")
driver.forward()
time.sleep(2)

print("현재 페이지 새로고침")
driver.refresh()
time.sleep(2)

print("현재 페이지의 스크린샷 저장")
driver.save_screenshot("save.png")
time.sleep(2)

print("브라우저 닫기")


# 현재 보고 있는 탭을 닫음
# 브라우저 내 탭이 하나였다면 탭을 닫으면서 브라우저도 닫힘
driver.close()
time.sleep(2)

# 브라우저 자체를 아예 닫아버림 (탭이 여러개 있었으면 강제로 다 닫힘)
# driver.quit()









# print(element)



#
# element = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[1]/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a')
# print(element)
#
# element = driver.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a')
# print(element)
#
# element = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[3]/c-wiz/div/div/div[1]/div/div/a')
# print(element)
#
# element = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[3]/c-wiz/div/div/div[1]/div/div/a')
# print(element)
#
# element = driver.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(3) > c-wiz > div > div > div.uzcko > div > div > a')







from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driverPath = "C:/Users/ITPS/Downloads/driver/chromedriver.exe"
URL = "https://www.google.com"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

element = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

element.send_keys("Tradingview")
time.sleep(1)

element = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.tfB0Bf > center > input.gNO89b')
element.click()

element = driver.find_element_by_css_selector('#rso > div:nth-child(1) > div > div > div > div.yuRUbf > a > h3')
element.click()

element = driver.find_element_by_css_selector('body > div.tv-main > div.tv-unauth-header > a')
element.click()

element = driver.find_element_by_css_selector('body > div.js-rootresizer__contents > div.layout__area--right > div > div.widgetbar-pages > div.widgetbar-pagescontent > div.widgetbar-page.active > div.widget-1quyc-Kt.widgetbar-widget.widgetbar-widget-detail > div.widgetbar-widgetbody > div > div.wrapper-3OdqYJdx > div.container-3PT2D-PK.widgetWrapper-2rvm3OC4.offsetDisabled-2rvm3OC4 > span.priceWrapper-3PT2D-PK > span.highlight-2GhssDiZ.price-3PT2D-PK')
print("현재 원/달러 환율가격 = ", element.text)

element = driver.find_element_by_css_selector('#js-category-content > div > div > div > div > div > div.tv-card-container__widgets.tv-sticky-columns__column.tv-sticky-columns__column--fix-bottom.tv-sticky-columns__column--layered > div:nth-child(1) > div > div.tv-feed-widget__body.js-widget-body > div > div:nth-child(1) > div.js-symbols-wrapper > div > div.js-quote-ticker.tv-site-table__row.tv-widget-watch-list__row.tv-site-table__row--interactive.tv-widget-watch-list__row--interactive.js-symbol-row-interactive.tv-site-table__row--highlighted.tv-widget-watch-list__row--highlighted.quote-ticker-inited > div.tv-widget-watch-list__quote-column.tv-site-table__column.tv-site-table__column--align_right.tv-site-table__column--last-phone-vertical > div.tv-widget-watch-list__last-wrap > div.tv-widget-watch-list__last.js-symbol-change-direction.js-symbol-last.apply-overflow-tooltip.up')
print("S&P", element.text)



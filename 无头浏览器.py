from selenium import webdriver
from time import sleep

# 实例化 options 对象
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.get('https://www.cnblogs.com/')

print(driver.page_source)
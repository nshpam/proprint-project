from bs4 import BeautifulSoup
from selenium import webdriver
import re
import requests
from fake_useragent import UserAgent
import undetected_chromedriver as uc


driver = uc.Chrome()
#ua = UserAgent()

template = 'https://www.hermes.com/th/en/category/women/bags-and-small-leather-goods/bags-and-clutches/#|'

#proxies_req = requests.request('https://www.sslproxies.org/')
#proxies_req.add_header('User-Agent', ua.random)
driver.get(template)

'''options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver.exe')
driver.get(template)

page = requests.get(template)

print(page.status_code)
print(driver.title)
'''


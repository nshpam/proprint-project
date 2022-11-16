from typing import Counter
from bs4 import BeautifulSoup
from bs4.element import PYTHON_SPECIFIC_ENCODINGS
from selenium import webdriver
import re
import sqlite3
search_keyword = input('Search: ')
driver = webdriver.Chrome(r'C:\Users\pam-s\anaconda3\Scripts\chromedriver.exe')

def get_url(search_word):
    template = 'https://www.advice.co.th/search?keyword={}'
    search_word = search_word.replace(' ','+')
    return template.format(search_word)

url = get_url(search_keyword)
driver.get(url)
ADVICE_website = BeautifulSoup(driver.page_source,'html.parser')

#get href
http = ADVICE_website.find_all('a',href=True)
href = []
for a_href in http:
    a_href = a_href["href"]
    href.append(str(a_href))

driver.quit()
#fliter1 : filtered duplicate elements
href = list(dict.fromkeys(href))

'''#fliter2 : filtered product
count = 0

for https in href:
    split_https = https.split('/')
    
    try:
        index = split_https.index('product')
    except ValueError:
        href[count] = ''

    count+=1

filter_object = filter(lambda x: x != "", href)
href = list(filter_object)'''

#filtered3 : filtered keywords
search_keyword = search_keyword.split()

filtered_website = []
count = 0

for webs in href:
    webs = webs.split('/')
    for web_str in webs:
        if web_str.find('-') != -1:
            web_str = re.sub('-',' ',web_str)
        web_str = web_str.split()
        for checking in web_str:
            if checking in search_keyword:
                filtered_website.append(href[count])
    count +=1

href = list(dict.fromkeys(filtered_website))
href.sort()

#write in text file
#FilePath = r'C:\Users\pam-s\Desktop\reference.txt'
FilePath = r'C:\Users\pam-s\Desktop\test2.txt'
ReadFile = open(FilePath,'a',encoding="utf-8")
for i in range(len(href)):
    ReadFile.write(href[i]+'\n')

print('finish')
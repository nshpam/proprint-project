from bs4 import BeautifulSoup
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

#Extract the collection
def JIB_Extraction(JIB_soruce):
    ADVICE_product_name = JIB_soruce.find_all('div',{'class':'product-name product-name-font'})
    ADVICE_product_price = JIB_soruce.find_all('div',{'class':'sale sale-font'})
    http = JIB_soruce.find_all('a')
    for href in http:
        ADVICE_product_href = href['href']
    #Delete Tags
    ADVICE = [ADVICE_product_name,ADVICE_product_price,ADVICE_product_href]
    
    for ADVICE_index in range(len(ADVICE)):
        for product in range(len(ADVICE[ADVICE_index])):
            #ADVICE[ADVICE_index][product] = re.sub('\n', ' ', str(ADVICE[ADVICE_index][product]))
            ADVICE[ADVICE_index][product] = re.sub(r'\s+', ' ',  str( ADVICE[ADVICE_index][product]))
            condition = re.findall('<',ADVICE[ADVICE_index][product])
            while condition != []:
                if ADVICE[ADVICE_index][product].find('<') != -1:
                    start_strip = ADVICE[ADVICE_index][product].find('<')
                    stop_strip = ADVICE[ADVICE_index][product].find('>')
                    strip_word = ADVICE[ADVICE_index][product][start_strip:stop_strip+1]
                    ADVICE[ADVICE_index][product] = re.sub(strip_word,'',ADVICE[ADVICE_index][product])
                else:
                    break
    return ADVICE

ADVICE_Information = {'ADVICE_name': JIB_Extraction(ADVICE_website)[0],'ADVICE_price':JIB_Extraction(ADVICE_website)[1],'ADVICE_href':JIB_Extraction(ADVICE_website)[2]}

print(ADVICE_Information['ADVICE_href'])

'''for product in range(len(JIB[ADVICE_index])):
    JIB[ADVICE_index][product] = re.sub('\n', ' ', str(JIB[ADVICE_index][product]))
    condition = re.findall('<',JIB[ADVICE_index][product])
        while condition != []:
            if JIB[ADVICE_index][product].find('<') != -1:
                start_strip = JIB[ADVICE_index][product].find('<')
                stop_strip = JIB[ADVICE_index][product].find('>')
                strip_word = JIB[ADVICE_index][product][start_strip:stop_strip+1]
                JIB[ADVICE_index][product] = re.sub(strip_word,'',JIB[ADVICE_index][product])
            else:
                break'''

'''ADVICE_website = BeautifulSoup(driver.page_source,'html.parser')

''#Extract the collection
def JIB_Extraction(JIB_soruce):
    ADVICE_product_name = JIB_soruce.find_all('span',{'class':'promo_name'})
    jib_product_details = JIB_soruce.find_all('div',{'class':'row description'})
    jib_product_price = JIB_soruce.find_all('p',{'class':'price_total'})

    #Delete Tags
    JIB = [ADVICE_product_name,jib_product_details,jib_product_price]

    for ADVICE_index in range(len(JIB)):
        for product in range(len(JIB[ADVICE_index])):
            JIB[ADVICE_index][product] = re.sub('\n', ' ', str(JIB[ADVICE_index][product]))
            condition = re.findall('<',JIB[ADVICE_index][product])
            while condition != []:
                if JIB[ADVICE_index][product].find('<') != -1:
                    start_strip = JIB[ADVICE_index][product].find('<')
                    stop_strip = JIB[ADVICE_index][product].find('>')
                    strip_word = JIB[ADVICE_index][product][start_strip:stop_strip+1]
                    JIB[ADVICE_index][product] = re.sub(strip_word,'',JIB[ADVICE_index][product])
                else:
                    break
    return JIB

JIB_Information = {'JIB_name': JIB_Extraction(ADVICE_website)[0],'JIB_details':JIB_Extraction(ADVICE_website)[1],'JIB_price':JIB_Extraction(ADVICE_website)[2]}

#https://www.jib.co.th/web/product/readProduct/28339/476/PRINTER--เครื่องพิมพ์ไร้สาย--HP-INKTANK-415'''
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import sqlite3

driver = webdriver.Chrome(r'C:\Users\pam-s\anaconda3\Scripts\chromedriver.exe')

def get_url(search_word):
    template = 'https://www.jib.co.th/web/product/product_search/0?str_search={}&cate_id[]='
    search_word = search_word.replace(' ','+')
    return template.format(search_word)

url = get_url('canon ink')
driver.get(url)
JIB_website = BeautifulSoup(driver.page_source,'html.parser')

#Extract the collection
def JIB_Extraction(JIB_soruce):
    jib_product_name = JIB_soruce.find_all('span',{'class':'promo_name'})
    #jib_product_href= JIB_soruce.find_all('a',{'title':'{}'})
    #https://www.jib.co.th/web/product/readProduct/20183/670/INK-REFILL-CANON--หมึกสำหรับเครื่องพิมพ์--GI-790M--MAGENTA-
    #https://www.jib.co.th/web/product/readProduct/20180/670/INK-REFILL-CANON--หมึกสำหรับเครื่องพิมพ์--GI-790BK--BLACK-
    jib_product_price = JIB_soruce.find_all('p',{'class':'price_total'})

    #Delete Tags
    JIB = [jib_product_name,jib_product_price]



    for JIB_index in range(len(JIB)):
        for product in range(len(JIB[JIB_index])):
            JIB[JIB_index][product] = re.sub('\n', ' ', str(JIB[JIB_index][product]))
            condition = re.findall('<',JIB[JIB_index][product])
            while condition != []:
                if JIB[JIB_index][product].find('<') != -1:
                    start_strip = JIB[JIB_index][product].find('<')
                    stop_strip = JIB[JIB_index][product].find('>')
                    strip_word = JIB[JIB_index][product][start_strip:stop_strip+1]
                    JIB[JIB_index][product] = re.sub(strip_word,'',JIB[JIB_index][product])
                else:
                    break
    return JIB

JIB_Information = {'JIB_name': JIB_Extraction(JIB_website)[0],'JIB_price':JIB_Extraction(JIB_website)[1]}

'''def create_table():
    conn = sqlite3.connect('ProPrint.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY, name TEXT, details TEXT, price INTEGER)''')
    conn.commit()
    conn.close()

def insert_table(name,detail,price):#ต้องใส่ข้อมูลให้ครบ
    conn = sqlite3.connect('ProPrint.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (NULL,?,?,?)", (name,detail,price))
    conn.commit()
    conn.close()

def update_table(id,name,detail,price):
    conn = sqlite3.connect('ProPrint.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET detail=?, price=?, name=? WHERE id=?',(detail,price,name,id))
    conn.commit()
    conn.close()

create_table()
for inserting1 in range(len(JIB_Information['JIB_name'])):
    insert_table(JIB_Information['JIB_name'][inserting1],JIB_Information['JIB_details'][inserting1],JIB_Information['JIB_price'][inserting1])

print('FINISH')'''
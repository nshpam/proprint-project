#Strip Test
from typing import Tuple

'''word = '<p class="price_total">\n4,990.-\n</p>'
strip_list = ['<','>','\n']

for strip_word in strip_list:
    x = word.find(strip_word)
    y = word[x+1:]
    
y = y.split('<')
print(y[0])'''

'''x = '<div class="row description">COLOR INKJET : PRINT / SCAN / COPY / WIRELESS </div>'
x = x.split('>')
x = x[1].split('<')
print(x[0])'''

'''word  = '4,990.-\n'
while True:
    if '\n' in word:
        strip_n = word.find('\n')
        word = word.strip(word[strip_n])
    else:
        break
print(word)'''


#options = webdriver.ChromeOptions() 
#options.add_argument("start-maximized")
#driver = uc.Chrome(options=options)
#driver.get(r'C:\Users\pam-s\anaconda3\Scripts\chromedriver.exe')

'''import re
print(re.__file__)'''
'''jib_product_price = ['<p class="price_total">\n4,990.-\n</p>','<p class="price_total">\n3,890.-\n</p>', 
'<p class="price_total">\n2,990.-\n</p>', '<p class="price_total">\n2,990.-\n</p>', 
'<p class="price_total">\n390.-\n</p>', '<p class="price_total">\n390.-\n</p>', 
'<p class="price_total">\n370.-\n</p>', '<p class="price_total">\n370.-\n</p>', 
'<p class="price_total">\n250.-\n</p>', '<p class="price_total">\n250.-\n</p>', 
'<p class="price_total">\n390.-\n</p>', '<p class="price_total">\n390.-\n</p>', 
'<p class="price_total">\n1,490.-\n</p>', '<p class="price_total">\n740.-\n</p>', 
'<p class="price_total">\n1,090.-\n</p>', '<p class="price_total">\n850.-\n</p>', 
'<p class="price_total">\n8,990.-\n</p>']
jib_product_name = '<span class="promo_name" style=" word-break: normal;">PRINTER (เครื่องพิมพ์ไร้สาย) HP INKTANK 415</span>\n<div class="row description">'
jib_product_details = 'COLOR INKJET : PRINT / SCAN / COPY / WIRELESS </div>'

JIB = [jib_product_price,jib_product_details,jib_product_name]
JIB_str = ['jib_product_price','jib_product_details','jib_product_name']

for JIB_list in range(len(JIB)):
    print('-------------THIS IS %s-------------'%JIB_str[JIB_list])
    print(JIB_list)
    #print(JIB[JIB_list])
    for sub in range(len(JIB[JIB_list])):
        try:
            print(JIB[JIB_list][sub])
        except IndexError:
            print(sub)
        else:
            print()'''


'''for sub in range(len(JIB)):
    JIB[sub] = re.sub('\n', ' ', JIB[sub])
    condition = re.findall('<',JIB[sub])
    while condition != []:
        if JIB[sub].find('<') != -1:
            start_strip = JIB[sub].find('<')
            stop_strip = JIB[sub].find('>')
            strip_word = JIB[sub][start_strip:stop_strip+1]
            JIB[sub] = re.sub(strip_word,'',JIB[sub])
        else:
            break
        
print(JIB)'''



'''if JIB[1].find('<') != -1:
            start_strip = JIB[1].find('<')
            stop_strip = JIB[1].find('>')
            strip_word = JIB[1][start_strip:stop_strip+1]
            JIB[1] = re.sub(strip_word,'',JIB[1])
        if JIB[2].find('<') != -1:
            start_strip = JIB[2].find('<')
            stop_strip = JIB[2].find('>')
            strip_word = JIB[2][start_strip:stop_strip+1]
            JIB[2] = re.sub(strip_word,'',JIB[2])'''
        
#print(JIB)

#print(word)
import re

word = 'INK REFILL CANON (หมึกสำหรับเครื่องพิมพ์) GI-790BK (BLACK)'
#https://www.jib.co.th/web/product/readProduct/20180/670/INK-REFILL-CANON--หมึกสำหรับเครื่องพิมพ์--GI-790BK--BLACK-

#https://www.jib.co.th/web/product/readProduct/20180/670/INK--REFILL--CANON--(หมึกสำหรับเครื่องพิมพ์)--GI-790BK--(BLACK)
#https://www.jib.co.th/web/product/readProduct/20180/670/INK--REFILL--CANON--หมึกสำหรับเครื่องพิมพ์--GI-790BK--BLACK

'''template = 'https://www.jib.co.th/web/product/readProduct/20180/670/{}'

iter_word = iter(word)
href = ''
for iteration in iter_word:
    print(iteration)
    if iteration == '(':
            iteration=''
            print('YES')
    if iteration == ')':
            iteration=''
            print('NO')
    else:
        href+=iteration

print(href)

def ChangeToRef(Change_name):
    template = 'https://www.jib.co.th/web/product/readProduct/20180/670/{}'
    iter_word = iter(word)
    href = ''
    for iteration in iter_word:
        if iteration == '(':
            iteration=''
        if iteration == ')':
            iteration=''
        else:
            href+=iteration
    
    href = href.replace(' ','--')
    return template.format(href)

url = ChangeToRef(word)
print(url)'''
'''word = ['https://www.advice.co.th/product/inkjet-all-in-one/canon/canon-pixma-g1010-plus-ink-tank','javascript:void(0)']

count = 0

word = list(dict.fromkeys(word))

for i in word:
    ii = i.split('/')
    print(ii)
    try:
        index = ii.index('product')
    except ValueError:
        word[count] = ''
        print(i)
    count+=1

filter_object = filter(lambda x: x != "", word)
word = list(filter_object)

print(word)'''

word = 'canon ink'
word = word.split()
#print(word)
website = [
    'https://www.advice.co.th/product/ink-refill-and-tank/refill-canon-original-/canon-gi-71-y',
    'https://www.advice.co.th/product/rack/patch-panel',
    'https://www.advice.co.th/product/rack/รางไฟ'
    ]

filtered_website = []
index = 0
for webs in website:
    webs = webs.split('/')
    for web_str in webs:
        if web_str.find('-') != -1:
            web_str = re.sub('-',' ',web_str)
        web_str = web_str.split()
        for checking in web_str:
            if checking in word:
                print('here')
                filtered_website.append(website[index])
    index +=1

filtered_website = list(dict.fromkeys(filtered_website))
filtered_website.sort()
print(filtered_website)
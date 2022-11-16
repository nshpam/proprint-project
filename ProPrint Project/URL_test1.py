import requests
from bs4 import BeautifulSoup

url = 'https://www.jib.co.th/web/product/readProduct/19112/672/INK-HP--%E0%B8%AB%E0%B8%A1%E0%B8%B6%E0%B8%81%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%9E%E0%B8%B4%E0%B8%A1%E0%B8%9E%E0%B9%8C--680--BLACK--F6V27AA'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
#header = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
web_data = requests.get(url,headers=header)
print(web_data.status_code)
#web_data.encoding = "utf-8"

print(web_data)

if web_data.status_code == 200:
    print("Successful")
elif web_data.status_code == 404:
    print("Error 404 page not found")
else:
    print("Not both 200 and 404")

#soup = BeautifulSoup(web_data.text, 'html.parser')#convert into html language
#print(soup.prettify())
'''
find_word = soup.find_all("h2",{"class":"price_inner"})'''


'''find_word = str(find_word)
print(find_word)'''

'''my user agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
'''
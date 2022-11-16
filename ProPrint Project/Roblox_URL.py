import requests
from bs4 import BeautifulSoup

url = 'https://www.roblox.com/users/650360953/profile'
web_data = requests.get(url)
print(web_data.status_code)

soup = BeautifulSoup(web_data.text, 'html.parser')#convert into html language

find_word = soup.find_all("h3",{"class":"profile-name text-overflow"})
#<h3 ng-bind="'Heading.AboutTab' | translate" class="ng-binding">About</h3>

find_word = str(find_word)
find_word = find_word.split()
#['[<h3', 'class="profile-name', 'text-overflow"', 'ng-non-bindable="">', 'NSHPAM5311', '</h3>]']

print(find_word[4])
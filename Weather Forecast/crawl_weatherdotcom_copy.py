import requests
import collections
from urllib.request import urlopen, Request
import pyexcel
from bs4 import BeautifulSoup

url     = "https://weather.com/vi-VN/weather/tenday/l/VMXX0006:1:VM"
# url     = "https://weather.com/vi-VN/weather/tenday/l/65bbbcbef8448c1f971408c74ed922af1bed94ddd8cc7a48d2bae40e75cef726"
# r       = requests.get(url)

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

webpage_text= webpage.decode("utf-8")
soup        = BeautifulSoup(webpage_text, "html.parser")

section     = soup.find('section', {'class': 'panel ls-24-hour-wrap twc-table-wrap card forecast-fiveday'})






# lấy dự báo (trời nhiều mây, có giống ,etc.)
td_des      = section.find_all('td', {'class': 'description'})
des_weather =[]
for td in td_des:
    span = td.span
    if span is not None:
        span = span.text
        des_weather.append(span.capitalize())
print(des_weather)

#Lấy nhiệt độ
td_temp     = section.find_all('td', {'class': 'temp'})
temp_weather = []
for td in td_temp:
    div     = td.div
    span    = div.find_all('span')
    for     _ in span:
        if  _ is not None and _.text != '':
            temp = _.text
            temp = temp.replace('°', '')
            temp_weather.append(temp)

high_weather = []
low_weather  = []
index_temp   = 0

for temp in temp_weather:
    index_temp += 1
    if index_temp % 2 == False:
        low_weather.append(temp)
    else:
        high_weather.append(temp)

print(temp_weather)

print(high_weather)
print(low_weather)



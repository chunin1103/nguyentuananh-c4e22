import requests
import collections
from urllib.request import urlopen, Request
import pyexcel
from bs4 import BeautifulSoup

url     = "https://weather.com/vi-VN/weather/tenday/l/VMXX0006:1:VM"


req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

webpage_text= webpage.decode("utf-8")
soup        = BeautifulSoup(webpage_text, "html.parser")
td 			= soup.find_all('td',{'class' :'twc-sticky-col'})
td1 			= soup.find_all('div',{'class' :'twc-table-shadow sticky'})
title 			= soup.find_all('title')
shit=[]
count=0
for i in td:

	shit.append(i.text)
for i in td1:

	shit.append(i)

for i2 in title:
	shit.append(i2)
print(shit)
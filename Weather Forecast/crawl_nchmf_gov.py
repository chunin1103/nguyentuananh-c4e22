import requests
import collections
from urllib.request import urlopen
from bs4 import BeautifulSoup


url     = "http://www.nchmf.gov.vn/web/vi-VN/62/19/58/map/Default.aspx"
r       = requests.get(url)

conn        = urlopen(url)
raw_data    = conn.read()
webpage_text= raw_data.decode("utf-8")
soup        = BeautifulSoup(webpage_text, "html.parser")

table   = soup.find("table", {'id': "_ctl1__ctl0__ctl0_dl_Thoitietthanhpho"})
td_list = table.find_all('td', {'class': "tieude_dubao_yeuto_content"})

# bóc description
des_gov = []
for td in td_list:
    div = td.div
    if div is not None:
        text = div.string
        text = text.replace("\r", '')
        text = text.replace("\t", '')
        text = text.replace("\n", '')
        des_gov.append(text)
print(des_gov)

# bóc nhiệt độ
strong = soup.find_all('strong')
temp_gov = []
index = 0
for _ in strong:
    data = _.string
    if data is not None and len(data) <= 4:
        temp_gov.append(data)
        index += 1
                       
print(temp_gov)


# Chia list nhiet do ra thanh sang va chieu
low_gov  = []
high_gov = []

for __ in range(0, len(temp_gov)):
        if __ + 1 > (len(temp_gov)/2):
                high_gov.append(temp_gov[__])
        else:
                low_gov.append(temp_gov[__])

print(low_gov)
print(high_gov)
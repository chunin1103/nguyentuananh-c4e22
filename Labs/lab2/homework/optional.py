from urllib.request import urlopen
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
from bs4 import BeautifulSoup

conn     = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup     = BeautifulSoup(webpage_text, "html.parser")

table = soup.find("table", {'id': 'tableContent'})
tr_list   = table.find_all("tr")

record_list = []
for tr in tr_list:
    td   = tr.td
    
    items= td.string

    data = OrderedDict({
        '': items,
    })
    record_list.append(data)

print(record_list)
pyexcel.save_as(records = record_list, dest_file_name = 'Fin Report.xlsx')

# Thiet lap ket noi -> Keo du lieu ve -> Giai ma du lieu do

# 1. Download webpage
from urllib.request import urlopen

url = "https://dantri.com.vn"
from bs4 import BeautifulSoup


# 1.1 Connect to website (open a connection)
conn = urlopen(url)
# 1.2 Download raw data
raw_data = conn.read()

# 1.3 Decode data
webpage_text = raw_data.decode("utf-8")


# 1.4 Save text 
    #f = file, w = write (thao tac ghi lai file)
    #wb = write binary
f = open("dantri.html", "wb")
f.write(raw_data)
f.close()

# 2. Extract ROI
    # 2.1 Convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser")
                        #Content        hieu la html
ul = soup.find("ul", "ul1 ulnew") # find("<element>", "attribute or class") # id = "ul1 ulnew"
# print(ul.prettify())    
    # print(soup.prettify())

li_list = ul.find_all("li")
# li = li_list[0]
news_list = []
for li in li_list:
    h4 = li.h4 # goi la walking, lay 1 element trong 1 parent
        # Khi
        # # <li>
        # #     <h4>
        # #         <a>
    a = li.h4.a
    title   = a.string #de lay content trong <a>
    link    = url + a["href"] #vao dict thi phai dung find()
    # print(title)
    # print(link)
    # print("*" * 20 )
    news = {
        "Title": title,
        "Link" : link,
    }
    news_list.append(news)
    print("*" * 20)

print(news_list)

# 3. Extract data

# 4. Save data



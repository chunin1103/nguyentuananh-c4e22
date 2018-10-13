from urllib.request import urlopen
import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs"
from bs4 import BeautifulSoup

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")

f = open("songs.html", "wb")
f.write(raw_data)
f.close()

soup = BeautifulSoup(webpage_text, "html.parser")

section = soup.find("section", {'class':"section chart-grid"})
ul      = section.find("ul")
li_list = ul.find_all("li")

song_list = []
for li in li_list:
    h3       = li.h3
    a_title  = li.h3.a
    h4       = li.h4
    a_artist = li.h4.a
    
    title    = a_title.string
    artist   = a_artist.string

    songs = OrderedDict({
        'Title': title,
        'Artist': artist,

    })
    song_list.append(songs)

print(song_list)
pyexcel.save_as(records = song_list, dest_file_name = "Song list.xlsx")
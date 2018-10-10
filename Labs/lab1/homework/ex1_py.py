from gmail import GMail, Message
from random import choice
import datetime

gmail = GMail('tuananh110397@gmail.com', 'Neji1234!')

html_template = '''
<p> Sep oi chet roi em bi {{ symptom }} mat roi </p>

<b>Sep ban giao ngay lai cong viec cho anh Huy va anh Quan ho em</b> <br>
<i>Em xin cam on va hau ta, co gi sep cu bao cao voi BO EM, Nguyen Phu Trong hoac thang den ONG NGOAI EM, Nguyen Xuan Phuc hoac ba noi em, Nguyen Thi Kim Tien
<br> Best regard </i>
'''

symptom_list = ['Tieu chay', 'Nho ny', 'Chan thoi']
html_content = html_template.replace("{{ symptom }}", choice(symptom_list))
msg          = Message('Xin nghi phep', to = 'chunin1103@gmail.com', html = html_content)

set_hour    = 23
set_minute  = 8
loop_counter= 0

while True:
    now         = datetime.datetime.now()

    if now.hour == set_hour and now.minute == set_minute:
        loop_counter += 1
        if loop_counter == 1:
            gmail.send(msg)
        loop_counter = 0


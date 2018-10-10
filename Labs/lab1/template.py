from gmail import GMail, Message
from random import choice

gmail   = GMail('tuananh110397@gmail.com','Neji1234!')

html_template = '''

<p> Sep oi chet roi em bi {{ symptom }} mat roi </p>

<b>Sep ban giao ngay lai cong viec cho anh Huy va anh Quan ho em</b> <br>
<i>Em xin cam on va hau ta, co gi sep cu bao cao voi BO EM, Nguyen Phu Trong hoac thang den ONG NGOAI EM, Nguyen Xuan Phuc hoac ba noi em, Nguyen Thi Kim Tien<i>
  
'''
symtom_list = ['Tieu chay', 'Nho ny', 'Chan thoi']
html_content = html_template.replace("{{ symptom }}", choice(symtom_list))
msg     = Message('Title',to='chunin1103@gmail.com', html = html_content) 

gmail.send(msg)


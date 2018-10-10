from gmail import GMail, Message

gmail   = GMail('tuananh110397@gmail.com','Neji1234!')
msg     = Message('Title',to='c4e.techkidsvn@gmail.com', html = html_content) 

html_content = '''
"<b>https://techkids.vn</b>",attachments=['programming.jpg'] )
<u>testing<u>
<p> đây là paragraph </p>

<b>https://techkids.vn</b> <br>
<i>testing<i>
  
'''

# <b> = bold
# <i> = italic
gmail.send(msg)
import smtplib
fromname='Dukes'

toname='myself'

subject='Testing my lab'

fromaddr = 'dukiemarshaw@gmail.com'

msg='Hello There,the fact that you have received this message means that my INFO3180 lab app works.'

toaddr = 'dukiemarshaw@yahoo.com'

message = """From: {} <{}>


To: {} <{}>

Subject: {}

{}

"""

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'dukiemarshaw@gmail.com'

password = 'gdenyclmlrefbrej'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()

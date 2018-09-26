import os, zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "atul4278@gmail.com"
# toaddr = "suhail.dandu@tele2.com"
toaddr = "atul4278@gmail.com"
# instance of MIMEMultipart
msg = MIMEMultipart()

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "5 best gainer\loser"

# string to store the body of the mail
body = "Body_of_the_mail - Test"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
attachment = open(xmlfile, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % xmlfile)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "XXXX")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()

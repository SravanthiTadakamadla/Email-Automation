import os
# Here are the email package modules we'll need
# Import smtplib for the actual sending function
import smtplib

import pandas as pd

from email.message import EmailMessage

# To make this email work we need to turn on less secure apps in gmail account
# Create the container email message.
msg = EmailMessage()
msg['Subject'] = 'Email Automation'

# Provision to add From email id
me = 'xyz@gmail.com'

# Read email ids from the excel file
read_emails = pd.read_excel("emailids.xlsx")
test_email_ids = read_emails['Emails'].values

dest_email_ids = test_email_ids
msg['From'] = me
msg['To'] = ', '.join(dest_email_ids)

files = open('Table_Animation.html').read()

# Provision to add customize HTML content 
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1 style="background:red;color:yellow;">Hello World</h1>
</body>
</html>
 """, subtype='html')


# Provision to add file as email content
msg.add_alternative(files, subtype='html')

# Module to read following extension types and add as an attachment to email
filesList = ('.jpg','.html','.csv','.py','.php','.png','.css')
my_files = [f.name for f in os.scandir() if f.name.endswith(filesList)]

for i in my_files:
	with open(i, 'rb') as f:
		file_data = f.read()
		file_name = f.name
	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


# Module to send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	
	smtp.login(me, 'password')
	smtp.send_message(msg)

	

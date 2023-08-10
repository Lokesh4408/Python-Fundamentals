import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

email = EmailMessage()
email['from'] = 'Balaji Harari'
email['to'] = 'andrei@zerotomastery.io'
email['subject'] = 'You won a lottery for 2000,000,000 euros today'

email.set_content('I am gonna be a python master')

with smtplib.SMTP(host= 'smtp.gmail.com', port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls() # an encryption mechanism
    smtp.login('balajiharari@gmail.com', 'Balajiharari!')
    smtp.send_message(email)
    print('all good boss!')

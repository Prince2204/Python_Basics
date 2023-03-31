#Sending email message from python

import smtplib

smtp_obj=smtplib.SMTP('smtp.gmail.com',587)

print(smtp_obj.ehlo())

print(smtp_obj.starttls())

import getpass

email=getpass.getpass("Email Please: ")
password=getpass.getpass("Password Please: ")
print(smtp_obj.login(email,password))

from_address=email
to_address=email
subject=input("Enter the email subject: ")
message=input("enter the body of email: ")
msg="Subject: "+subject+"\n"+message

smtp_obj.sendmail(from_address,to_address,msg)

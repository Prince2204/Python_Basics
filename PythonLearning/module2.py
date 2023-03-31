#range, in, enumarate, zip,
#random   : randint, shuffle
#input
#list comprehension
#generator
#iterator
#decorators
#timeit
#zip and unzip files

#Python Libraries:
#zipfile, shutil, random, 
import imaplib
import getpass
import email

M=imaplib.IMAP4_SSL("imap.gmail.com")
e_mail=getpass.getpass("Email Please: ")
password=getpass.getpass("Password Please: ")
print(M.login(e_mail,password))
print(M.list())
print(M.select("INBOX"))

typ, data=M.search(None,'SUBJECT "WELCOME TO PYTHON"')
print(typ)
print(data)

email_id=data[0]
print("email id is: ",email_id)
result, email_data=M.fetch(email_id,'(RFC822)')
raw_email=email_data[0][1]
raw_email_string=raw_email.decode('utf-8')
email_message=email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body=part.get_payload(decode=True)
        print(body)



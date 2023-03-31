import imaplib
import getpass
import email

M=imaplib.IMAP4_SSL("imap.gmail.com")

#GET EMAIL AND PASSWORD
e_mail=getpass.getpass("Email Please: ")
password=getpass.getpass("Password Please: ")

#use credentials passed above to login to email
print(M.login(e_mail,password))
# List all the folders on email
print(M.list())
#selecting Inbox folder
print(M.select("INBOX"))
# searching the email with a subject line "WELCOME TO PYTHON"
typ, data=M.search(None,'SUBJECT "WELCOME TO PYTHON"')
print(typ)
print(data)

email_id=data[0]
print("email id is: ",email_id)
#Fetching the email based on the id in data
result, email_data=M.fetch(email_id,'(RFC822)')
#getting the raw email 
raw_email=email_data[0][1]
#decoding the raw email to raw string
raw_email_string=raw_email.decode('utf-8')
#getting the email message from raw string
email_message=email.message_from_string(raw_email_string)
# walking through the email message to get the actual message
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body=part.get_payload(decode=True)
        print(body)




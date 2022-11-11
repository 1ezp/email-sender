import smtplib,ssl
from email.message import EmailMessage



context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)



def login(username,password):
    response = server.login(username,password)
    if "2.7.0 Accepted" not in str(response):
        print("Error login.")
        exit()

def send(From,to,subject,body):
    email = EmailMessage()
    email['From'] = From
    email["To"] = to
    email["Subject"] = subject
    email.set_content(body)
    response = server.sendmail(From,to,email.as_string())
    
    
username = input("Login email: ")
password = input("Login Password: ")
subject = input("Title: ")
body = input("Message: ")
emails = open("emails.txt",'r').read().splitlines()
done = 0


login(username,password)
for email in emails:
    send(username,email,subject,body)
    done += 1
    print(f"Email sent to {email} as well.")

print(f"Total emails {done}")



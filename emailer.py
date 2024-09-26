import os
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

# save user/pw info in .env in same dir
from dotenv import load_dotenv
load_dotenv()

def send_mail(send_from,send_to,subject,text,files,server,port,username='',password='',isTls=True):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    #part.set_payload(open("cnp1.csv", "rb").read())
    part.set_payload(open(files, "rb").read())
    encoders.encode_base64(part)
    #part.add_header('Content-Disposition', 'attachment; filename="cnp1.csv"')
    part.add_header('Content-Disposition', 'attachment; filename=files')
    msg.attach(part)

    # context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    # SSL connection only working on Python 3+
    smtp = smtplib.SMTP(server, port)
    if isTls:
        smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

 
port = 587 
server = "smtp.gmail.com"
#send_from = os.getenv("send_from")
#send_to = os.getenv("send_to") 
#password = os.getenv("password")
#password=""
#subject = "test"
#text = "teXt"
#files = ""

# main driver
if __name__ == '__main__':
    # send the email with csv file attachment from same dir ('cnp1.csv')
    
    send_to=input("To: ")
    print("\n")
    send_from=input("from: ")
    print("\n")
    password=input("Password: ")
    print("\n")
    subject=input("Subject: ")
    print("\n")
    text=input("Text message: ")
    print("\n")
    files=input("Attach file path to be sent: ")
    print("\n")
    print(server,"\n", send_from,"\n", send_to)
    send_mail(send_from,send_to,subject,text,files,server,port,username=send_from,password=password,isTls=True)

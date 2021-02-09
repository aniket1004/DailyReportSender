import schedule
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendReport(body):
    me = "swapnil.febina1@gmail.com"
    password = "Swapnil@1708@"
    to = "kunal.febina@gmail.com"
    cc = "divfebinagroup@gmail.com,hr.febinagroup@gmail.com"
    rcpt = cc.split(",") + [to]
    msg = MIMEMultipart('alternative')
    msg['From'] = me
    msg['Subject'] = "Daily Report"
    msg['To'] = to
    msg['Cc'] = cc
    body = MIMEText(body)
    msg.attach(body)
    try:
        smtplibobj = smtplib.SMTP('smtp.gmail.com',587)
        smtplibobj.starttls()
        smtplibobj.login(me,password)
        smtplibobj.sendmail(msg['From'],msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
        print ("Success")
    except:
        print("Failed to send daily report")

def main():
    fd = open("report.txt", "r")
    body = fd.read()
    schedule.every().day.at("18.40").do(sendReport,body)
    time.sleep(30)
    while(True):
        schedule.run_pending()

if __name__ == "__main__":
    main() 
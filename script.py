import pandas as pd
import smtplib

SenderAddress = "Your email"
password = "your google app secure password"

e = pd.read_excel("real_moveIn_sheet.xlsx")
emails = e['Email'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a test from a python script."
subject = "Hello from python test"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
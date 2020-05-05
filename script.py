import pandas as pd
import smtplib

SenderAddress = "chuymedina96@gmail.com"
# Use app password
password = "password of sender"

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
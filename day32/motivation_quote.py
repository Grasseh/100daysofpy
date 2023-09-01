import smtplib
import datetime as dt
import os
import random

now = dt.datetime.now()
quotes = ['dummy']
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

if not os.path.isfile('quotes.txt'):
    now = dt.datetime(year=2023, month=8, day=22) # Tuesday
else:
    with open('quotes.txt', mode="r") as file:
        quotes = file.readlines()

sender = "Motivational Monday <steve@grasseh.com>"
receiver = "Stevo <steve@grasseh.com>"
quote = random.choice(quotes)

message = f"""\
Subject: Motivational Quote
To: {receiver}
From: {sender}

#{quote}"""

# import ipdb; ipdb.set_trace()
if now.weekday() == 0: # Monday
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        print(server.login(USERNAME, PASSWORD))
        print(server.sendmail(sender, receiver, message))

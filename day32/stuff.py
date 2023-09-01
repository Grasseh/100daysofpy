import smtplib
import datetime as dt

now = dt.datetime.now()
print(now.year)
birthday = dt.datetime(year=1994, month=10, day=8)

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("18e2ed35f05695", "5f02b5bd5afa22")
    # server.sendmail(sender, receiver, message)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import os
import random
import pandas

def send_birthday_wish(birthday, template):
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    name = birthday['name']
    email = birthday['email']
    sender = "Stevo <steve@grasseh.com>"
    receiver = f"{name} <{email}>"
    content = template.replace('[NAME]', name)

    message = f"""\
Subject: Happy Birthday
To: {receiver}
From: {sender}

{content}"""

    # import ipdb; ipdb.set_trace()

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        print(server.login(username, password))
        print(server.sendmail(sender, receiver, message))

now = dt.datetime.now()
templates_dir = 'letter_templates'
template = ''

files = [f for f in os.listdir(templates_dir) if os.path.isfile(f"{templates_dir}/{f}")]
file = random.choice(files)
with open(f"{templates_dir}/{file}", mode="r") as file:
    template = file.read()

now = dt.datetime.now()

birthdays = pandas.read_csv('birthdays.csv')

birthdays = [ {
    'date' : dt.datetime(year= r.year, month= r.month, day= r.day),
    'name' : r.full_name,
    'email' : r.email
} for (i, r) in birthdays.iterrows() if r.month == now.month and r.day == now.day]

for birthday in birthdays:
    send_birthday_wish(birthday, template)


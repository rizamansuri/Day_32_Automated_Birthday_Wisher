# BismillahirRahmanirRahim
from datetime import datetime
import pandas as pd
import random
import smtplib

my_email = "riza.mansuri11@gmail.com"
password = "kuvlwrgfjoksicqr"
today = (datetime.now().month, datetime.now().day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    with open(random.choice(letter_list)) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy birthday!\n\n{contents}"
        )




import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv


load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
RECIEVER_EMAIL = os.getenv("RECIEVER_EMAIL")

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIEVER_EMAIL,
                msg=f"Subject:Monday Motivation\n\n{quote}"
            )







##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas
import smtplib
import datetime as dt

# My email and password
my_email = "shermantaymkmk@gmail.com"
my_password = "Shertayman1998"

# reading the today date time
current_day = dt.datetime.now()

# Read CSV file
with open("birthdays.csv") as file:
    birthday_details = pandas.read_csv(file)
    bd_dict = birthday_details.to_dict("records")
    for data in bd_dict:
        if data['month'] == current_day.month and data['day'] == current_day.day:

            # Choosing a random letter
            letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                           "letter_templates/letter_2.txt"]
            with open(random.choice(letter_list), mode="r+") as file:
                chosen_letter = file.read().replace('[NAME]', f"{data['name']}")

            # Establish a connection
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=data['email'],
                    msg=f"Subject:Happy Birthday!\n\n{chosen_letter}"
                )

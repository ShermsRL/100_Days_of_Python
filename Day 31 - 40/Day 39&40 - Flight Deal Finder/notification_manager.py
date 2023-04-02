from twilio.rest import Client
import smtplib


class NotificationManager():
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "-"
        self.auth_token = "-"
        self.twilio_num = "-"
        self.phone_num = "-"
        self.email = "-"
        self.password = "-"

    def price_alert(self, price, from_city, from_city_code, to_city, to_city_code, from_date, to_date):
        client = Client(self.account_sid, self.auth_token)
        alert = client.messages.create(
            body=f"Low price alert! Only ${price} to fly from {from_city}-{from_city_code} to "
                 f"{to_city}-{to_city_code}, from {from_date} to {to_date}",
            from_=self.twilio_num,
            to=self.phone_num
        )

    def send_emails(self, link, price, from_city, from_city_code, to_city, to_city_code, from_date, to_date):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs="shermantaymk@gmail.com",
                msg=f"Subject: New low Price Flight!\n\nLow price alert! Only ${price} from "
                    f"{from_city}-{from_city_code} to {to_city}-{to_city_code} from {from_date} to {to_date}. "
                    f"Link: {link}"
            )

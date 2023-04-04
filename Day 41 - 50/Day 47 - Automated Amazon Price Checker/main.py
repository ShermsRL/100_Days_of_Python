from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

gmail_email = "shermantaymkmk@gmail.com"
gmail_password = "-"
PRODUCT_LINK = "https://www.amazon.com/dp/B0863TXGM3?tag=camelproducts-20&linkCode=ogi&th=1&language=en_US"
TARGET_PRICE = 250.0

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(
    url=PRODUCT_LINK,
    headers=header
)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find("span", class_="a-offscreen")
price_num = float(price.get_text().split("$")[1])
product = soup.find(id="productTitle").get_text()


if price_num <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail_email, password=gmail_password)
        connection.sendmail(
            from_addr=gmail_email,
            to_addrs="shermantaymk@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n {product} is now {TARGET_PRICE} or lower!\n {PRODUCT_LINK}",
        )
import datetime
from twilio.rest import Client
import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

newsapi = "-"
stockapi = "-"

# Twilio account info
account_sid = "-"
auth_token = "-"
client = Client(account_sid, auth_token)

yesterday = datetime.date.today()-datetime.timedelta(1)
day_before_yesterday = datetime.date.today()-datetime.timedelta(2)

stock_price_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stockapi,

}

news_parameters = {
    "q": "tesla",
    "apikey": newsapi,
    "country": "us",
}

news_dict = {}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url= 'https://www.alphavantage.co/query', params=stock_price_parameters)
stock_data = stock_response.json()

yesterday_stock_price = float(
    stock_data['Time Series (60min)']
    [f'{yesterday} 20:00:00']
    ['4. close']
)
day_before_yesterday_stock_price = float(
    stock_data['Time Series (60min)']
    [f'{day_before_yesterday} 20:00:00']
    ['4. close']
)

percentage_different = ((yesterday_stock_price-day_before_yesterday_stock_price)
                        / day_before_yesterday_stock_price) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_response = requests.get(url='https://newsapi.org/v2/top-headlines', params=news_parameters)
news_data = news_response.json()
if percentage_different >= 5 or percentage_different <= -5:
    for num in range(3):
        news_dict[f'Headline{num}'] = news_data['articles'][num]['title']
        news_dict[f'Brief{num}'] = news_data['articles'][num]['description']
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
client.messages.create(
    body=f"'{STOCK}: {percentage_different}%\nHeadline: {news_dict['Headline1']}\nBrief: {news_dict['Brief1']}'"
         f"\n\nHeadline: {news_dict['Headline2']}\nBrief: {news_dict['Brief2']}'"
         f"\n\nHeadline: {news_dict['Headline3']}\nBrief: {news_dict['Brief3']}'",
    from_="+18302712293",
    to="+6597622109"
)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


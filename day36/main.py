import requests
import os
import smtplib
import ipdb
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def get_variation(stock):
    ALPHA_URL = 'https://www.alphavantage.co/query'
    ALPHANTAGE_KEY = os.environ.get('ALPHANTAGE_KEY')
    alpha_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': ALPHANTAGE_KEY
    }

    response = requests.get(ALPHA_URL, params=alpha_params)
    response_json = response.json()
    last_data_date = response_json['Meta Data']['3. Last Refreshed']
    daily_data = response_json['Time Series (Daily)'][last_data_date]
    open_score = float(daily_data['1. open'])
    close_score = float(daily_data['4. close'])
    return (close_score / open_score * 100) - 100

def get_news(company_name):
    NEWS_API_URL = 'https://newsapi.org/v2/everything'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    news_params = {
        'q': company_name,
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API_KEY,
        'pageSize': 3
    }

    response = requests.get(NEWS_API_URL, params=news_params)
    response_json = response.json()

    return [
        {
            "title": article['title'],
            "brief": article['description']
        }
        for article in response_json['articles']
    ]

def send_email(news, variation):
    username = os.environ.get('MAILTRAP_USERNAME')
    password = os.environ.get('MAILTRAP_PASSWORD')
    sender = "Stevo <steve@grasseh.com>"
    receiver = f"Stevo <steve@grasseh.com>"

    message = f"""\
Subject: STOCK PRICE VARIANCE
To: {receiver}
From: {sender}

{STOCK}: {variation}

Headline: {news[0]['title']}

Brief: {news[0]['brief']}

Headline: {news[1]['title']}

Brief: {news[1]['brief']}

Headline: {news[2]['title']}

Brief: {news[2]['brief']}"""

    # ipdb.set_trace()
    print(message)
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        print(server.login(username, password))
        print(server.sendmail(sender, receiver, message.encode('utf-8')))

variation = get_variation(STOCK)
print(variation)

if abs(variation) >= 5.0:
    news = get_news(COMPANY_NAME)
    send_email(news, variation)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# NAAAAH I'LL USE AN EMAIL I DON'T WANNA GIVE TWILIO CREDIT CARD INFO

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


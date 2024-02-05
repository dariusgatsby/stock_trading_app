import requests
import os
from datetime import date
from datetime import timedelta
import send_sms
from math import ceil


def check_min_difference(num1, num2):
    # Calculate the percentage difference
    percentage_difference = abs(float(num1) - float(num2)) / ((float(num1) + float(num2)) / 2) * 100
    if percentage_difference == 0.0:
        return None
    return ceil(percentage_difference)


today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=6)

NEWS_APIK = os.environ.get("NEWS_APIK")
STOCK_APIK = os.environ.get("STOCK_APIK")
STOCK = "TSLA"

news_params = {
    "q": "tesla",
    "apiKey": NEWS_APIK,
    "from": yesterday,
    "pageSize": 3,

}
stock_params = {
    "symbol": STOCK,
    "apikey": STOCK_APIK,
}

stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
stock_response = requests.get(stock_url, params=stock_params)

stock_data = stock_response.json()
print(stock_data)
last_refresh = stock_data["Meta Data"]["3. Last Refreshed"]
yesterday_price = stock_data["Time Series (Daily)"][last_refresh]['4. close']
day_before_yesterday_price = stock_data["Time Series (Daily)"][str(day_before_yesterday)]['4. close']

price_dif = check_min_difference(yesterday_price, day_before_yesterday_price)
print(price_dif)

news_response = requests.get("https://newsapi.org/v2/top-headlines", params=news_params)
data = news_response.json()['articles']


if price_dif >= 2:
    news_response = requests.get("https://newsapi.org/v2/top-headlines", params=news_params)
    print(news_response.json())
    j = 0
    messages = []
    for i in messages:
        while j < len(data):
            title = data[j]['title']
            description = data[j]['description']
            url = data[j]['url']
            if price_dif >= 2:
                message = f"{STOCK} 🔺{price_dif}%\n{title}'\n'{description}'\n'{url}\n\n"
                messages.append(message)
            elif price_dif <= 2:
                message = f"{STOCK} 🔻{price_dif}%\n{title}'\n'{description}'\n'{url}\n\n"
                messages.append(message)
            j += 1
        print(i)
        # send_sms.send_message(i)



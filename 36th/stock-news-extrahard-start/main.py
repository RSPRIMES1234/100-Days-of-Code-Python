import requests
from datetime import date,timedelta
from twilio.rest import Client

account_sid = ';adfjkjkl;asasdl;jasd;jk'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)
#########################################################################################################
yesterday=str(date.today()-timedelta(days=1))
day_before_yesterday=str(date.today()-timedelta(days=2))
print(yesterday,day_before_yesterday)
#########################################################################################################
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY=";'jklasadl;''asdio"
news_param={
"function":"NEWS_SENTIMENT",
    "tickers":STOCK,
    "limit":"3",
    "apikey":API_KEY
}
#########################################################################################################
price_up_down=requests.get(url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey=jkl;ad;ajkld')
price_up_down.raise_for_status()
prices=price_up_down.json()["Time Series (Daily)"]
yesterday_price=float(prices[str(yesterday)]['4. close'])
day_before_yesterday_price=float(prices[str(day_before_yesterday)]['1. open'])
print(yesterday_price,day_before_yesterday_price)
price_change=day_before_yesterday_price-yesterday_price
price_percentage=round(price_change/day_before_yesterday_price)
#########################################################################################################



if price_change>(0.01)*day_before_yesterday_price:
    news=requests.get(url="https://www.alphavantage.co/query",params=news_param)
    news.raise_for_status()
    news_title=news.json()["feed"][0]["title"]
    new_summary=news.json()["feed"][0]["summary"]
    if price_change>0:
        message = client.messages.create(
            body=f"""TSLA: 🔺{price_percentage}%
        Headline: {news_title} (TSLA)?. 
        Brief:  {new_summary}""",
            from_='+1800000000',
            to='+91000000000'
        )
    else:
        message = client.messages.create(
            body=f"""TSLA: 🔻{price_percentage}%
Headline: {news_title} (TSLA)?. 
Brief: {new_summary}""",
            from_='+180000000',
            to='+91000000000'
        )
#########################################################################################################


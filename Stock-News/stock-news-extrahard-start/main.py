STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key_alphavantage = "9RJ7USBED1Q15KGJ"
newsapi_key = "8c0e4a3b6c9447669ff066b2dfd3ccb3"
import requests

parameters = {
     "function" : "TIME_SERIES_DAILY",
     "symbol" : STOCK,
     "apikey" : "9RJ7USBED1Q15KGJ",
 }


response = requests.get(url = 'https://www.alphavantage.co/query',params=parameters)
response.raise_for_status()

data_yesterday = float(response.json()["Time Series (Daily)"]["2022-02-11"]["4. close"])
data_daybefore = float(response.json()["Time Series (Daily)"]["2022-02-10"]["4. close"])
difference = data_yesterday - data_daybefore
a = round(((difference/data_yesterday)*100),2)


news_parameters ={
    "apiKey" : newsapi_key,
    "q": "Tesla",

}
news_response = requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
news_response.raise_for_status()
news_titles = []

for i in range(1,4):
    news_title = news_response.json()["articles"][i]["title"]
    news_titles.append(news_title)

fall = False

if a<0:
    a = a*(-1)
    fall = True

if fall:
    price = f"{a}% 🔻"
else:
    price = f"{a}% 🔺"



news_content = news_response.json()["articles"][1]["description"]


account_sid = "AC7654559c307150ae2c4afc90ae17e2c3"
auth_token = "a40132edb82649ce8a42e930bb7b0c20"
phone_no = "+18455236702"

from twilio.rest import Client


client = Client(account_sid, auth_token)

message = client.messages \
          .create(
                              body=f"TSLA: {price}\nHeadline:{news_titles[0]}\nBrief:{news_content}",
                              from_=phone_no,
                              to="+918123789765"
          )
print(message.status)

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


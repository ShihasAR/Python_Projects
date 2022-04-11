import requests
from twilio.rest import Client

account_sid = "Aqqqq"
auth_token = "cccccc"
phone_no = "nnnnn"
BACK_UP = "qwwqwqwww"

parameters = {

   "lat" : 60.391262,
   "lon" : 5.322054,
   "appid" : "hhhhhhh",
   "exclude" : "current,minutely,daily"
  }
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)

will_rain = False

for i in range(0,13):
  ID = response.json()["hourly"][i]["weather"][0]["id"]
  if int(ID) < 700:
      will_rain = True


if will_rain:
      client = Client(account_sid, auth_token)
      message = client.messages \
          .create(
          body="It's going to rain, carry an umbrella.",
          from_= phone_no,
          to= "nnmggggg",
      )
      print(message.status)




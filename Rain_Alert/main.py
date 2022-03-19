import requests
from twilio.rest import Client

account_sid = "AC7654559c307150ae2c4afc90ae17e2c3"
auth_token = "a40132edb82649ce8a42e930bb7b0c20"
phone_no = "+18455236702"
BACK_UP = "0viWVBrTmYX-OfVsZUoZNIYdsdcrzr0Vbt_B17Hm"

parameters = {

   "lat" : 60.391262,
   "lon" : 5.322054,
   "appid" : "9c73a187212d081309d03718175a05d2",
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
          to= "+918123789765",
      )
      print(message.status)



